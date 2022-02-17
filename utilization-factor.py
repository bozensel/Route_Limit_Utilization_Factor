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

with open("user_pass.txt", "r") as f5:
        user_pass = f5.readlines()

for list_user_pass in user_pass:
        if "username" in list_user_pass:
                username = list_user_pass.split(":")[1].strip()
        if "password" in list_user_pass:
                password = list_user_pass.split(":")[1].strip()

def ssh(nodeip):
        try:
                huawei = {
                        'device_type': 'huawei', 'ip': nodeip, 'username':
                        username, 'password': password, }
                con = Netmiko(**huawei)
                print(nodeip.strip() + "  " + "successful login")
        except Exception as e:
                print(e)
                f_3.write(nodeip.strip() + "\n")
                return

#******************************************
        
        data_to_parse_0 = con.send_command_timing('display ip vpn-instance | ignore-case i Customer_A') 

        print(data_to_parse_0)

        ttp_template_0 ="""
  {{Customer_Name}}                             {{nodeip}}     {{IPV4}}
"""
        parser_0 = ttp(data=data_to_parse_0, template=ttp_template_0)
        parser_0.parse()

        #print result in JSON format
        results_0 = parser_0.result(format='json')[0]
        print(results_0)

        #str to list **convert with json.loads
        result_0 = json.loads(results_0)
        print(result_0[0]["Customer_Name"])

        #******************************************
        data_to_parse = con.send_command_timing("display current-configuration configuration vpn-instance  {}".format(result_0[0]["Customer_Name"]))
        print(data_to_parse)

        ttp_template ="""
  {{routing-table}} limit {{ total_number | DIGIT }} {{total_number2}}

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

        data_to_parse_2 = con.send_command_timing('dis ip routing-table vpn-instance' + " " + result_0[0]["Customer_Name"] + " " + " statistics | i Summary Prefixes")

        print(data_to_parse_2)

        ttp_template_2 ="""
Summary Prefixes : {{ used_number | DIGIT }}
"""

        parser2 = ttp(data=data_to_parse_2, template=ttp_template_2)
        parser2.parse()

        #print result in JSON format
        results2 = parser2.result(format='json')[0]
        print(results2)

        #str to list **convert with json.loads
        result2 = json.loads(results2)
        print(result2[0]["used_number"])

#******************************************

        result3 = (int(result2[0]["used_number"]) / int(result[0]["total_number"])) * 100
        print(int(result3))

        with open("vrf_limit_result.txt", "a") as f:
                f.write("Customer_Result" +"_" + nodeip +"==>" + str(result3)+ "\n")
                f.close()

#******************************************

f_2 = open("ip_list.txt", "r")
ip_list = f_2.readlines()
f_2.close()
f_3 = open("Ssh_unconnected_2.txt", "w")

# Therading method
myPool = ThreadPool(100)
result = myPool.map(ssh, ip_list)
