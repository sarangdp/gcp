# compute engine template

"""Creates compute engine template"""


def GenerateConfig(unused_context):
    """Creates the Compute Engine with network and firewall."""

    resources = [{
        'name': 'vm-1',
        'type': 'vm-template.py'
    }, {
        'name': 'vm-2',
        'type': 'vm-template-2.py'
    }, {
        'name': 'network-1',
        'type': 'network-template.py'
    }, {
        'name': 'firewall-1',
        'type': 'firewall-template.py'
    }]

    return {'resources': resources}
