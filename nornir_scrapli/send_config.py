from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_config_to_node(task):
    task.run(task=send_config, config="ntp server 145.239.5.94")


results = nr.run(task=send_config_to_node)

print_result(results)
