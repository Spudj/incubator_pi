#!/usr/bin/python
################################################################################
## - Setup script for basic incubator operation protocol.                     ##
## - Jasen Finch 14/03/2015                                                   ##
################################################################################

import subprocess

print "Updating system.."
subprocess.call("sudo apt-get update",shell = True)
subprocess.call("sudo apt-get upgrade",shell = True)
## Install bcm2835 library
print "Installing C libraries"
subprocess.call("sh bcm2835_install.sh",shell = True)
## Compile C code
subprocess.call("gcc Adafruit_DHT.c -o Adafruit_DHT.o -std=c99 -I. -lbcm2835",shell = True)
## Set up necessary python modules
print "Installing necessary python modules.."
subprocess.call("sudo apt-get install python-dev",shell = True)
subprocess.call("sudo apt-get install python-pip",shell = True)
subprocess.call("sudo pip install RPi.GPIO",shell = True)
