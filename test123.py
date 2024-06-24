from netmiko import ConnectHandler

device1 = {
	"device_type":"cisco_ios",
	"ip":"192.168.10.11",
	"username":"admin",
	"password":"Cisco123"
}

device2 = {
	"device_type":"cisco_ios",
	"ip":"192.168.10.12",
	"username":"admin",
	"password":"Cisco123"
}

device3 = {
	"device_type":"cisco_ios",
	"ip":"192.168.10.13",
	"username":"admin",
	"password":"Cisco123"
}

# x = ConnectHandler(**device)
# output = x.send_command("show ip int br")
# print(output)


# config_commands = ["conf t", "int lo0", "ip add 1.1.1.1 255.255.255.255"]
with open("config1.txt", "w") as f:
	configs = f.read().splitlines()
	print(configs)
	
# Configure all devices
all_devices = [device1, device2, device3]
for device in all_devices:
	x = ConnectHandler(**device)
	output = x.send_config_set(configs)
	print(output)

# Configure new VLANs
	for n in range(50,101):
		vlan = str(n)
		print("Creating VLAN " + vlan)
		vlan_commands = ["vlan " + vlan, "name Python_VLAN_" + vlan]
		output = x.send_config_set(vlan_commands)
		print(output)

