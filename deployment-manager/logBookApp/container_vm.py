COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'

def ZonalComputeUrl(project, zone, collection, name):
    return ''.join([COMPUTE_URL_BASE,
                    'projects/',
                    project,
                    '/', zone,
                    '/', collection,
                    '/', name])

def GlobalComputeUrl(project, collection, name):
    return ''.join([COMPUTE_URL_BASE,
                    'projects/', project,
                    '/global/', collection,
                    '/', name])

def GenerateConfig(context):

    BASE_NAME = context.env['name']

    instance = {
        'zone': context.properties['zone'],
        'machineType': ZonalComputeUrl(context.env['project'],context.properties['zone'], 'machineTypes', 'f1-micro'),
        'metadata': {
            'items': [{
                'key': 'gce-container-declaration',
                'value': GenerateConfig(context)
            }]
        },
        'disk': [{
            'deviceName': 'boot',
            'type': 'PERSISTENT',
            'autoDelete': True,
            'boot': True,
            'initializeParams': {
                'diskName': BASE_NAME + '-disk',
                'sourceImage': GlobalComputeUrl('cos-cloud', 'images', context.properties['containerImage'])
            }
        }],
        'networkInterfaces': [{
            'accessConfigs': [{
                'name': 'external-nat',
                'type': 'ONE_TO_ONE_NAT'
            }],
        'network': GlobalComputeUrl(context.env['project'], 'networks', 'default')
        }],
        'serviceAccounts': [{
            'email': 'default',
            'scopes': ['https://www.googleapis.com/auth/logging.write']
        }]
    }

    resources = {
        'resources': [{
            'name': BASE_NAME,
            'type': 'compute.v1.instance',
            'properties': instance
        }]
    }

    return resources
