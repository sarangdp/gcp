"""Creates the Compute Engine."""

NETWORK_NAME = 'a-custom-network'


def GenerateConfig(context):
  """Creates the Compute Engine with multiple templates."""

  resources = [{
      'name': 'the-first-vm',
      'type': 'vm-template-var.py',
      'properties': {
          'machineType': 'f1-micro',
          'zone': 'us-central1-f',
          'network': NETWORK_NAME
      }
  }, {
      'name': 'the-second-vm',
      'type': 'vm-template-var.py',
      'properties': {
          'machineType': 'f1-micro',
          'zone': 'us-central1-f',
          'network': NETWORK_NAME
      }
  }, {
      'name': NETWORK_NAME,
      'type': 'network-template-var.py'
  }, {
      'name': NETWORK_NAME + '-firewall',
      'type': 'firewall-template-var.py',
      'properties': {
          'network': NETWORK_NAME
      }
  }]
  return {'resources': resources}
