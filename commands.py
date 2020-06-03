commands = [
    {
        'command': 'vpn_on',
        'shell_command': './assets/connect_vpn.sh',
        'use_response': True
    },
    {
        'command': 'vpn_off',
        'shell_command': './assets/disconnect_vpn.sh',
        'text': 'VPN apagada'
    },
    {
        'command': 'vpn_ip',
        'shell_command': 'ifconfig tun0 | head -n2 | tail -n1 | awk \'{print $2}\'',
        'use_response': True,
        'text': 'No se encuentra ninguna ip'
    }
]
