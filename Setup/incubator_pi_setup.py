##*********************************************************
## incubator_pi_setup.py
## 26-05-2014
##*********************************************************

import subprocess

print("Updating system...")
subprocess.call("sudo apt-get update",shell=True)
subprocess.call("sudo apt-get upgrade",shell=True)

## Set up necessary python modules
print("Installing necessary python modules...")
subprocess.call("sudo apt-get install python-dev",shell=True)
subprocess.call("sudo apt-get install python-pip",shell=True)
subprocess.call("sudo pip install RPi.GPIO",shell=True)
subprocess.call("sudo pip install rpy2",shell=True)
#subprocess.call("sudo pip install matplotlib",shell=True)
#subprocess.call("sudo pip install pandas",shell=True)
#subprocess.call("sudo pip install numpy",shell=True)

## Set up R and necessary packages
print ("Installing R and necessary packages...")
subprocess.call("sudo apt-get install r-base-core",shell=True)
subprocess.call("Rscript R_packages_setup.R",shell=True)


