import serial

ser = serial.Serial('COM3', 9600)  # Adjust port and baud rate
while True:
    data = ser.readline().decode().strip()
    print("Received:", data)
