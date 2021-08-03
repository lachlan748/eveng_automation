from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

ntp = "145.239.5.94"

configs = [f"ntp server vrf MGMT {ntp}", 
           f"ip route vrf MGMT {ntp} 255.255.255.255 192.168.137.1"]

def send_configs_to_node(task):
    task.run(task=send_configs, configs=configs)


results = nr.run(task=send_configs_to_node)

print_result(results)
