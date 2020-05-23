"""Creates network template"""

def GenerateConfig(context):

    resources = [{
        'name': 'a-new-network',
        'type': 'compute.v1.network',
        'properties': {
            'routingConfig': {
                'routingMode': 'REGIONAL'
            },
            'autoCreateSubnetworks': True
        }
    }]

    return {'resources': resources}
