#!/usr/bin/python3

import optparse       #to list help menu options
import subprocess     #to execute commands just like in the terminal

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "Enter the interface")
parser.add_option("-m", "--mac", dest = "new_mac", help = "Enter new mac address")

(options, arguments) = parser.parse_args()       #maps options and arguments
interface = options.interface
new_mac = options.new_mac

print("Changing MAC Address on " + str(interface) + " to " + str(new_mac))

subprocess.call(["ifconfig", str(interface), "down"])
subprocess.call(["ifconfig", str(interface), "hw", "ether", str(new_mac)])
subprocess.call(["ifconfig", str(interface), "up"])
