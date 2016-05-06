(function() {
  var config = 'STATSD_CONFIG' in process.env ? JSON.parse(process.env.STATSD_CONFIG) : {};
  config.servers = [
    {
      server: './servers/udp',
      address: '0.0.0.0',
      port: 8125
    }
  ];
  config.mgmt_address = '0.0.0.0';
  config.mgmt_port = 8126;
  config.log = {
    backend: 'stdout'
  };
  config.automaticConfigReload = false;

  return config;
})();
