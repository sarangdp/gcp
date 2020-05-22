COMPUTE_URL_BASE= 'https://www.googleapis.com/compute/v1/'

## The template must define a method called GenerateConfig(context) or generate_config(context). 
## If you use both method names in the same template, the generate_config() method will take precedence.

def GenerateConfig(unused_context):
    """Creates the first virtual machine"""

    resources = [{
        'name': 'the-first-vm',
        'type': 'compute.v1.instance',
        'properties': {
            'zone':'us-central1-f',
            'machineType': ''.join([COMPUTE_URL_BASE, 'projects/cloud-guru-sarang',
                                  '/zones/us-central1-f/',
                                  'machineTypes/f1-micro']),
            'disks': [{
                'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                          'debian-cloud/global/',
                                          'images/family/debian-9'])
              }
            }],
            'networkInterfaces': [{
              'network': '$(ref.a-new-network.selfLink)',
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
            }]
        }
    }]

    ## The method must return a Python dictionary
    return {'resources': resources}
