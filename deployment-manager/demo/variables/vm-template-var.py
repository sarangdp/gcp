COMPUTE_URL_BASE= 'https://www.googleapis.com/compute/v1/'

# Valid environment variables include the deployment name, the project ID, 
# the name property of your resource,
# and the type of your configuration. 

def GenerateConfig(context):
    """Creates the first virtual machine"""

    resources = [{
        'name': context.env['name'],
        'type': 'compute.v1.instance',
        'properties': {
            'zone': context.properties['zone'],
            'machineType': ''.join([COMPUTE_URL_BASE, 'projects/',
                                  context.env['project'],
                                  '/zones/',
                                  context.properties['zone'],
                                  '/machineTypes/',
                                  context.properties['machineType']]),
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
              'network': '$(ref.' + context.properties['network'] + '.selfLink)',
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
            }]
        }
    }]

    ## The method must return a Python dictionary
    return {'resources': resources}
