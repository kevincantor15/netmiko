from netmiko import ConnectHandler # Importing ConnectHandler from netmiko to handle network device connections

# Define device configurations for three Cisco IOS devices
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

# Open and read the configuration file. Read and split lines from config file into a list
with open("config1.txt", "w") as f:
	configs = f.read().splitlines()
	print(configs)
	
# List of all device configurations
all_devices = [device1, device2, device3]

# Iterate over each device to apply configurations
for device in all_devices:
	x = ConnectHandler(**device)  # Establish a connection to the current device
	output = x.send_config_set(configs) # Send configuration commands from config file
	print(output)

	# Create VLANs 50 to 100
	for n in range(50,101):
		vlan = str(n)  # Convert VLAN number to string
		print("Creating VLAN " + vlan)
		vlan_commands = ["vlan " + vlan, "name Python_VLAN_" + vlan]
		output = x.send_config_set(vlan_commands)  # Send VLAN creation commands to the device
		print(output)

