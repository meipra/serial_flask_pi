from flask import Flask, render_template
import datetime
import serial
import time
import signal
import sys

app = Flask(__name__)

ser = serial.Serial("/dev/ttyUSB0", 4800)

def signal_handler(signal, frame):
	ser.close()
	sys.exit(0)

@app.route("/")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y %H:%M")
	templateData = {
		'title' : 'Hello',
		'time' : timeString
		}
	return render_template('index.html', **templateData)

@app.route("/on", methods=['POST'])
def on():
	print(chr(155) + "abcdef" + chr(85))
	ser.write(chr(155) + "abcdef" + chr(85))
	ser.flush()
	return "on"

@app.route("/off", methods=['POST'])
def off():
	print(chr(155) + "zabcde" + chr(105))
	ser.write(chr(155) + "zabcde" + chr(105))
	ser.flush()
	return "off"

if __name__ == "__main__":
	if (ser.is_open):  ser.close()
	ser.open()
	signal.signal(signal.SIGINT, signal_handler)
	app.run(host='0.0.0.0', port=80, debug=True)
