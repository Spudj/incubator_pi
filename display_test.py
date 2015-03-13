
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
import sys



lcd = Adafruit_CharLCD()

lcd.begin(16,1)

while(True):

	
	lcd.clear()
	lcd.message(datetime.now().strftime('%b %d   %H:%M\n'))
	sleep(55)