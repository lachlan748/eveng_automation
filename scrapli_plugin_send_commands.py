from nornir import InitNornir
from nornir_scrapli.tasks import send_commands

from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

commands = ["show ip route", "show ip bgp summary", "show ntp status"]

def show_commands_test(task):
    task.run(task=send_commands, commands=commands)

result = nr.run(task=show_commands_test)

print_result(result)
