import serial

def serial_communication(port_name, baud_rate, data_to_send):
    """
    Simple serial communication function for LabVIEW Python Node
    Inputs:
        port_name: string (e.g., 'COM1')
        baud_rate: integer (e.g., 9600)
        data_to_send: string to send
    Returns:
        received_data: string of received data
    """
    try:
        # Open serial port
        ser = serial.Serial(
            port=port_name,
            baudrate=baud_rate,
            timeout=1
        )
        
        # Send data
        ser.write(data_to_send.encode())
        
        # Read response
        received_data = ser.read(100).decode()  # Read up to 100 bytes
        
        # Close port
        ser.close()
        
        return received_data
    
    except Exception as e:
        return f"Error: {str(e)}"
