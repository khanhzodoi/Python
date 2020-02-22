from netmiko import ConnectHandler


cisco = {
	'device_type': 'cisco_ios',
	'ip': '10.10.10.6',
	'username': 'khanhzodoi', 
	'password': 'dkmvng', 
	'secret': 'cisco',
}
device = ConnectHandler(**cisco)

print("Before config push")

print("Enter enable mode")
device.enable()

output = device.send_command("show startup-config")
print(output)

configcmds=["line vty 0 4", "logging synch"]
device.send_config_set(configcmds)

configcmds=["interface fastEthernet 0/0", "description primary network"]
device.send_config_set(configcmds)

print("Make sure to save config!!!")

output = device.send_command("wr")
print(output)

print ("After config push")


output = device.send_command("show startup-config")
with open('demo_log.txt', 'a') as log :
    print(output + "\n" + 10*"===", file=log)

print("Disconnect ssh connection")
device.disconnect()
