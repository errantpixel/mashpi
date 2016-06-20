import kivy
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

import RPi.GPIO as GPIO

# Set up GPIO:
pump1Pin = 17
pump2Pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump1Pin, GPIO.OUT)
GPIO.output(pump1Pin, GPIO.LOW)
GPIO.setup(pump2Pin, GPIO.OUT)
GPIO.output(pump2Pin, GPIO.LOW)

# Define some helper functions:

# This callback will be bound to the LED toggle and Beep button:
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


class MyApp(App):

	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)

		# Make the background gray:
		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(800,600), pos=layout.pos)

		# Create the rest of the UI objects (and bind them to callbacks, if necessary):
		Pump1Control = ToggleButton(text="Pump 1", background_color(1,0,0,1))
		Pump1Control.bind(on_press=press_callback)
		Pump2Control = ToggleButton(text="Pump 2")
		Pump2Control.bind(on_press=press_callback)
		wimg = Image(source='logo.png')

		# Add the UI elements to the layout:
		layout.add_widget(wimg)
		layout.add_widget(Pump1Control)
		layout.add_widget(Pump2Control)

		return layout

if __name__ == '__main__':
	MyApp().run()
