import serial
import time

ser = serial.Serial('COM3', 9600)  # Adjust port and baud rate

while True:
    ser.write(b'Hello LabVIEW\n')  # Send message to LabVIEW
    time.sleep(1)
