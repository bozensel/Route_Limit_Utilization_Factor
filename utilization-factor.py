from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from ttp import ttp
from genie.testbed import load
from pprint import pprint
import json
import time
from multiprocessing.dummy import Pool as ThreadPool
from netmiko import Netmiko
#******************************************

with open("username_password.txt", "r") as a5:
        username_password = a5.readlines()

for list_username_password in username_password:
        if "username" in list_username_password:
                username = list_username_password.split(":")[1].strip()
        if "password" in list_username_password:
                password = list_username_password.split(":")[1].strip()

def ssh(nodeip):
        try:
                nokia = {
                        'device_type': 'nokia', 'ip': nodeip, 'username':
                        username, 'password': password, }
                con = Netmiko(**nokia)
                print(nodeip.strip() + "  " + "successful login")
        except Exception as e:
                print(e)
                n_1.write(nodeip.strip() + "\n")
                return


#******************************************
        con.send_command_timing('environment no more')
        data_to_parse_1 = con.send_command_timing('show service service-using') 

        print(data_to_parse_1)

        ttp_template_1 = """
<group name="VPRN_ID">
{{serviceID}}           {{service_Type}}      {{ignore}}   {{ignore}}   {{ignore}}          {{ignore}}
</group>
"""

parser_1 = ttp(data=data_to_parse_1, template=ttp_template_1)
parser_1.parse()

# print result in JSON format
results1 = parser_1.result(format='json')[0]
#print(results)

#converting str to json. 
result1 = json.loads(results1)

vprn_id = []

for i in result1[0]['VPRN_ID']:# Created a list (vprn_id) which only includes vprn ids. 
    if i['service_Type'] == 'VPRN':
        vprn_id.append(i['serviceID'])

# print(vprn_id) 

        #******************************************
	for j in vprn_id:
        data_to_parse = con.send_command_timing("show router {} bgp neighbor 172.16.24.2 detail".format(j))
        print(data_to_parse)

ttp_template = """
<group name="Active_Prefixes">
IPv4 active          : {{ipv4|DIGIT}}             IPv6 active          : {{ipv6|DIGIT}}
VPN-IPv4 active      : {{vpn-ipv4|DIGIT}}            VPN-IPv6 active      : {{vpn-ipv6|DIGIT}}  
Label-IPv4 active    : {{label-ipv4|DIGIT}}                Label_IPv6 active    : {{label-ipv6|DIGIT}}    
MVPN-IPv4 active     : {{mvpn-ipv4|DIGIT}}                MVPN-IPv6 active     : {{mvpn-ipv6|DIGIT}}    
Mcast-IPv4 active    : {{mcast-ipv4|DIGIT}}                Mcast-IPv6 active    : {{mcast-ipv6|DIGIT}}    
L2-VPN active        : {{l2-vpn|DIGIT}}                EVPN active          : {{evpn|DIGIT}}
</group>
<group name="Prefix_Limit">
{{family}}           {{prefix_limit|DIGIT}}     {{ignore}}        {{ignore|DIGIT}}        {{ignore}}  {{ignore}}
</group>
"""

parser = ttp(data=data_to_parse, template=ttp_template)
        parser.parse()

        #print result in JSON format
        results = parser.result(format='json')[0]
        print(results)

        #str to list **convert with json.loads
        result = json.loads(results)
        print(result)

#******************************************

        result3 = int(result[0]['Active_Prefixes']['ipv4'])/int(result[0]['Prefix_Limit'][0]['prefix_limit'])*100
        print(int(result3))

        with open("vprn_limit_result.txt", "a") as f:
                f.write("Customer_Result" +"_" + nodeip +"==>" + str(result3)+ "\n")
                f.close()

#******************************************

n_2 = open("ip_list.txt", "r")
ip_list = n_2.readlines()
n_2.close()
n_1 = open("Ssh_unconnected_2.txt", "w")

# Therading method
myPool = ThreadPool(100)
result = myPool.map(ssh, ip_list)

#**********************************************
#Sample json output after the data is parsed:

“””
[
    {
        "Active_Prefixes": {  
            "evpn": "0",      
            "ipv4": "9999",   
            "ipv6": "6643432",
            "l2-vpn": "0",    
            "mcast-ipv4": "0",
            "mcast-ipv6": "0",
            "mvpn-ipv4": "0",
            "mvpn-ipv6": "0",
            "vpn-ipv4": "45223",
            "vpn-ipv6": "5674363"
        },
        "Prefix_Limit": [
            {
                "family": "ipv4",
                "prefix_limit": "1000000000"
            },
            {
                "family": "evpn",
                "prefix_limit": "10000000"
            }
        ]
    }
]
“””
