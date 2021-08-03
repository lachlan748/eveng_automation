from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

ntp = "185.208.170.29"

commands = [f"ntp server vrf MGMT {ntp}",
            f"ip route vrf MGMT {ntp} 255.255.255.255 192.168.137.1"]

def send_config_to_node(task):
   task.run(task=netmiko_send_config, config_commands=commands) 

results = nr.run(task=send_config_to_node)

print_result(results)
