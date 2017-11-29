from flask import Flask, render_template
import datetime
import serial
import time
import signal
import sys

app = Flask(__name__)

ser = serial.Serial("/dev/ttyACM0", 4800)

if (ser.is_open): ser.close()
ser.open()

while True:
	time.sleep(1)
	ser.write("abcdef")
	ser.flush()
	time.sleep(1)
	ser.write("zabcde")
	ser.flush()

