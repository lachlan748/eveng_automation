from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="./config.yaml")

def send_command_to_node(task):
    task.run(task=netmiko_send_command, command_string="show ip bgp")

results = nr.run(task=send_command_to_node)

print_result(results)
