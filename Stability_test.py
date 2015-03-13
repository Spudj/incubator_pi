##*******************************************************************
## incubator_pi.py
## Jasen Finch
## 11/05/2014
## Initial control script for logging and analysing temperature and humidity data
## Takes humidity and temperature readings, logs them and displays them on LCD display
##*******************************************************************
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import RPi.GPIO as GPIO
import subprocess
import os
import datetime
import sys

GPIO.setwarnings(False)

## Functions
def measure (pin):
	while (True):
		temp_str = subprocess.check_output(["sudo","./DHT_sensor", "22", str(pin)])
		if (len(temp_str) == 77):
			break

	temp = temp_str[55:59]
	hum = temp_str[70:74]
	date_today = str(datetime.date.today())
	time_now = str(datetime.datetime.now().time())
	data = [str(date_today),str(time_now[0:8]),str(temp),str(hum)]
	return data

def Stability_test (pin, hours):
	if int(hours) > 24:
		raise Exception("Numbers of hours cannot exceed 24")
	
	## Set up LCD
	lcd = Adafruit_CharLCD()
	lcd.begin(16,1)
	lcd.clear()
	
	## Open file for writing data
	name_date = str(datetime.date.today())
	name_time = str(datetime.datetime.now().time())
	name_str = name_date + "_data.csv"
	data_file = open(name_str,"w")
	data_file.write("Date,Time,Temperature (*C),Humidity (%)\n")
	
	## Calculate end time
	start_time = name_time[0:5]
	if hours == 24:
		end_time = start_time
	else:
		end_hour = int(start_time[0:2]) + int(hours)
		if end_hour >= 24:
			end_hour = end_hour - 24
		if end_hour < 10:
			end_time = "0" + str(end_hour) + ":" + start_time[3:5]
		else:
			end_time = str(end_hour) + ":" + start_time[3:5]
	print "Start time: " + start_time
	print "End time: " + end_time
	print "Please wait..."
	lcd.message("Please Wait...")
	## Read temperature and humidity
	sleep(61)
	print "Beginning data collection"
	while True:
		time = str(datetime.datetime.now().time())
		time_now = time[0:5]
		if time_now == end_time:
			break
		else:
			data = measure(pin)
			data_file.write(data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "\n")
			lcd.clear()
			lcd.message(time_now + "  StabTest\n")
			lcd.message("T:" + data[2] + "*C" + " H:" + data[3] + "%") 
			sleep(59)

	data_file.close()
	print "Data collection complete"
	Path = os.getcwd()
	R_cmd = "Rscript incubator_pi_plot.R " + Path + " " + name_str
	print "Plotting data..."
	subprocess.call(R_cmd, shell=True)
	lcd.clear()
	lcd.message("Stability test\n")
	lcd.message("complete")
	print "Stability test complete."

pin = sys.argv[1]
hours = sys.argv[2]
Stability_test(pin,hours)