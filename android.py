import random

import kivy
import serial
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

# Set up the serial connection with Arduino
arduino = serial.Serial("COM3", baudrate=9600, timeout=1)
def read_from_arduino():
    """Reads distance data from Arduino and updates the display."""
    try:
        # Read data from Arduino (Assuming Arduino sends data as integers)
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()  # Read the data as a string
            return float(data)

    except Exception as e:
        print(f"Error reading from Arduino: {e}")




class MyRoot(BoxLayout):

    label_color1 = ListProperty([1, 1, 1, 1])
    label_color2 = ListProperty([1, 1, 1, 1])
    label_color3 = ListProperty([1, 1, 1, 1])
    label_color4 = ListProperty([1, 1, 1, 1])
    label_color5 = ListProperty([1, 1, 1, 1])
    label_color6 = ListProperty([1, 1, 1, 1])

    def update(self, dt):

        data = read_from_arduino()
        if data is None:
            return
        print(data)
        if data <20:
            self.label_color1 = ([1,0,0,1])
            self.label_color2 = ([1, 1, 1, 1])
            self.label_color3 = ([1, 1, 1, 1])
            self.label_color4 = ([1, 1, 1, 1])
            self.label_color5 = ([1, 1, 1, 1])
            self.label_color6 = ([1, 1, 1, 1])
        elif data >= 20 and data <40:
            self.label_color1 = ([1, 1, 1, 1])
            self.label_color2 = ([1, 0, 0, 1])
            self.label_color3 = ([1, 1, 1, 1])
            self.label_color4 = ([1, 1, 1, 1])
            self.label_color5 = ([1, 1, 1, 1])
            self.label_color6 = ([1, 1, 1, 1])
        elif data >= 40 and data < 80:
            self.label_color1 = ([1, 1, 1, 1])
            self.label_color2 = ([1, 1, 1, 1])
            self.label_color3 = ([1, 0.5, 0, 1])
            self.label_color4 = ([1, 1, 1, 1])
            self.label_color5 = ([1, 1, 1, 1])
            self.label_color6 = ([1, 1, 1, 1])
        elif data >= 80 and data < 140:
            self.label_color1 = ([1, 1, 1, 1])
            self.label_color2 = ([1, 1, 1, 1])
            self.label_color3 = ([1, 1, 1, 1])
            self.label_color4 = ([1, 0.5, 0, 1])
            self.label_color5 = ([1, 1, 1, 1])
            self.label_color6 = ([1, 1, 1, 1])
        elif data >=140 and data <200:
            self.label_color1 = ([1, 1, 1, 1])
            self.label_color2 = ([1, 1, 1, 1])
            self.label_color3 = ([1, 1, 1, 1])
            self.label_color4 = ([1, 1, 1, 1])
            self.label_color5 = ([1, 1, 0, 1])
            self.label_color6 = ([1, 1, 1, 1])
        elif data >= 200 and data < 400:
            self.label_color1 = ([1, 1, 1, 1])
            self.label_color2 = ([1, 1, 1, 1])
            self.label_color3 = ([1, 1, 1, 1])
            self.label_color4 = ([1, 1, 1, 1])
            self.label_color5 = ([1, 1, 1, 1])
            self.label_color6 = ([1, 1, 0, 1])
        else:
            self.label_color1 = ([1, 1, 1, 1])
            self.label_color2 = ([1,1,1,1])
            self.label_color3 = ([1,1,1,1])
            self.label_color4 = ([1,1,1,1])
            self.label_color5 = ([1,1,1,1])
            self.label_color6 = ([1,1,1,1])








    def __init__(self):
        super(MyRoot, self).__init__()

        Clock.schedule_interval(self.update, 0.1)

class MyApp(App):



    def build(self):
        return MyRoot()

myapp = MyApp()
myapp.run()
