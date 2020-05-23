"""Create firewall for firewalls"""

def GenerateConfig(context):
    """Create firewall for firewalls"""

    resources = [{
        'name': 'a-firewall-rule',
        'type': 'compute.v1.firewall',
        'properties': {
            'network': '$(ref.a-new-network.selfLink)',
            'sourceRanges': ['0.0.0.0/0'],
            'allowed': [{
                'IPProtocol': 'TCP',
                'ports': [80]
            }]
        }
    }]

    return {'resources': resources}
