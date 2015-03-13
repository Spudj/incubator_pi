import os 

net_name = raw_input("Network Name: ")
net_pass = raw_input("Password: ")

file = "/etc/network"

os.chdir(file)
int = open("interfaces","a")
str_1 = "\nauto wlan0\niface wlan0 inet dhcp\n\twpa-ssid " + net_name + "\n\twpa-psk " + net_pass

int.write(str_1)
