# mashpi
# 2016.06.20 - chorton@gmail.com
#
#
# Core Stuff
import os, os.path, sys
import time
import datetime

# Kivy Imports

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty

# GPIO Imports

import RPi.GPIO as GPIO

# Set up GPIO:
pump1Pin = 17
pump2Pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump1Pin, GPIO.OUT)
GPIO.output(pump1Pin, GPIO.LOW)
GPIO.setup(pump2Pin, GPIO.OUT)
GPIO.output(pump2Pin, GPIO.LOW)


# Set up the callbacks for the buttons/toggles

def press_callback(obj):
	if obj.text == 'Pump 1':
		if obj.state == "down":
			print ("button on")
			GPIO.output(pump1Pin, GPIO.HIGH)
		else:
			print ("button off")
			GPIO.output(pump1Pin, GPIO.LOW)
	if obj.text == 'Pump 2':
		if obj.state == "down":
			print ("button on")
			GPIO.output(pump2Pin, GPIO.HIGH)
		else:
			print ("button off")
			GPIO.output(pump2Pin, GPIO.LOW)

# w1 sensors.
# mlt = mashtun temp sensor
# hlt = Hot Liquor Tank sensor
# blk = Boil Kettle sensor
# chl = post-chiller (NPT threaded) sensor
#
# Note: Sensor values will change if device replaced. Update to match environment.
# #
#
# from w1thermsensor import W1ThermSensor
#
# mlt_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000007c157ee")
# hlt_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000007c2aacc")
# blk_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000007350eb1")
# chl_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0315718597ff")
#
# # Set some defaults
#
# mlt_temp = 42
# hlt_temp = 42
# blk_temp = 42
# chl_temp = 42
#
# # To get temp from a sensor (once), set the following function
# # mlt_temp = mlt_sensor.get_temperature(W1ThermSensor.DEGREES_F)
#
# def update_temps(dt):
# 	mlt_temp = mlt_sensor.get_temperature(W1ThermSensor.DEGREES_F)
# 	hlt_temp = mlt_sensor.get_temperature(W1ThermSensor.DEGREES_F)
# 	blk_temp = mlt_sensor.get_temperature(W1ThermSensor.DEGREES_F)
# 	chl_temp = mlt_sensor.get_temperature(W1ThermSensor.DEGREES_F)

# Do the thing with the stuff

class MyApp(App):

	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=3)

		# Make the background gray:
		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(800,600), pos=layout.pos)

		# Set up the refresh/Clock
		# Clock.schedule_interval(update_temps, 5.0)

		# Create the rest of the UI objects (and bind them to callbacks, if necessary):
		Pump1Control = ToggleButton(text="Pump 1")
		Pump1Control.bind(on_press=press_callback)
		Pump2Control = ToggleButton(text="Pump 2")
		Pump2Control.bind(on_press=press_callback)
		wimg = Image(source='logo.png')
		# labelMLT = Label(text=str(mlt_temp))

		# Add the UI elements to the layout:
                layout.add_widget(Label(text="HLT: 170.4",
					font_size=52))
                layout.add_widget(Label(text=''))
                layout.add_widget(Label(text="MLT: 154.3",
					font_size=52))
                layout.add_widget(Label(text="Boil: 212.0",
					font_size=52))
                layout.add_widget(Label(text=''))
                layout.add_widget(Label(text="Chill: 76.5",
					font_size=52))
		layout.add_widget(Pump1Control)
		layout.add_widget(wimg)
		layout.add_widget(Pump2Control)
		# layout.add_widget(labelMLT)


		return layout

if __name__ == '__main__':
	MyApp().run()
