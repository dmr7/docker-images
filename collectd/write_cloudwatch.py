import os, signal, collectd, boto3.session, botocore.client
from datetime import datetime
from fnmatch import fnmatch

def key_value_pairs(str):
    pairs = map(lambda s: s.split('=', 1), filter(bool, str.split(',')))
    if any(len(p) != 2 for p in pairs):
        raise ValueError('malformed key/value list: {}'.format(str))
    return pairs

class GlobMap(object):
    def __init__(self, entries):
        self.entries = dict(entries)

    def set(self, key, value):
        self.entries[key] = value

    def get(self, key, default=None):
        if key in self.entries:
            return self.entries[key]
        for k, v in self.entries.iteritems():
            if fnmatch(key, k):
                return v
        return default

class Config(object):
    def __init__(self):
        self.aws_region = os.environ.get('AWS_REGION', None)
        self.units = GlobMap({
            # Standard types
            'absolute': 'Count',
            'counter': 'Count/Second',
            'derive': 'Count/Second',
            'gauge': 'Count',
            'uptime': 'Seconds',

            # Spring
            'gauge.gc.*.time': 'Milliseconds',
            'gauge.heap': 'Kilobytes',
            'gauge.heap.committed': 'Kilobytes',
            'gauge.heap.init': 'Kilobytes',
            'gauge.heap.used': 'Kilobytes',
            'gauge.instance.uptime': 'Milliseconds',
            'gauge.mem': 'Kilobytes',
            'gauge.mem.free': 'Kilobytes',
            'gauge.nonheap': 'Kilobytes',
            'gauge.nonheap.committed': 'Kilobytes',
            'gauge.nonheap.init': 'Kilobytes',
            'gauge.nonheap.used': 'Kilobytes',
            'gauge.uptime': 'Milliseconds'
        })
        for k, v in key_value_pairs(os.environ.get('WC_UNITS', '')):
            self.units.set(k, v)

        self.dimensions = [dict(Name=n, Value=v) for n, v in key_value_pairs(os.environ.get('WC_DIMENSIONS', ''))]

def metrics(vl, config):
    set = vl.type_instance
    dims = list(config.dimensions)
    units = config.units

    if vl.plugin == 'statsd':
        prefix, _, set = set.partition('.')
        if len(set) == 0:
            set = prefix
        else:
            dims.append(dict(Name='Prefix', Value=prefix))
    elif not set:
        set = vl.type

    sources = collectd.get_dataset(vl.type)
    if len(sources) == 1:
        _, type, _, _ = sources[0]
        unit = units.get(type, 'None')
        unit = units.get('.'.join([type, set]), unit)
        yield (set, unit, dims)
    else:
        for name, type, _, _ in sources:
            name = '.'.join([set, name])
            unit = units.get(type, 'None')
            unit = units.get('.'.join([type, set]), unit)
            unit = units.get('.'.join([type, name]), unit)
            yield (name, unit, dims)

def plugin_config(cfg, config):
    for node in cfg.children:
        if node.key == 'aws_region':
            config.aws_region = node.values[0]
        if node.key == 'units':
            for unit in node.children:
                config.units.set(unit.key, unit.values[0])
        if node.key == 'dimensions':
            for dim in node.children:
                config.dimensions.append(dict(Name=dim.key, Value=dim.values[0]))

def plugin_write(vl, config):
    session = boto3.session.Session(region_name=config.aws_region)
    client_config = botocore.client.Config(connect_timeout=5, read_timeout=5)
    client = session.client('cloudwatch', config=client_config)
    metrics_list = list(metrics(vl, config))
    ts = datetime.fromtimestamp(vl.time)
    data = []

    for i, v in enumerate(vl.values):
        fullname, unit, dims = metrics_list[i]
        name = fullname[:255]
        if len(name) < len(fullname):
            collectd.warning('Metric name was truncated for CloudWatch: {}'.format(fullname))

        data.append(dict(
            MetricName=name,
            Timestamp=ts,
            Value=v,
            Unit=unit,
            Dimensions=dims
        ))

    client.put_metric_data(Namespace=vl.plugin, MetricData=data)

def plugin_init():
    collectd.info('Initializing write_cloudwatch')
    signal.signal(signal.SIGCHLD, signal.SIG_DFL)

config = Config()
collectd.register_config(plugin_config, config)
collectd.register_init(plugin_init)
collectd.register_write(plugin_write, config)
