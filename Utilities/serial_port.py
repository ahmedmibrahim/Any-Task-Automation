# Run it as follows:
#    serial = SerialPort("COM10")
#    cmd = serial.send_cmd("cmd")

# Necessary packages
import sys, traceback, time
try: 
    import serial as serial    # For COM Port
except:
    print ('ERROR: pyserial not installed -> Run in command line: pip install serial')
try:
    import visa                # For Equipment
except:
    print ('ERROR: pyvisa not installed -> Run in command line: pip install pyvisa')


class SerialPort(object):
    def __init__(self, com_port="COM4", baudrate=115200, timeout=0.1,
                 parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                 bytesize=serial.EIGHTBITS):
        try:
            self.serial_port = serial.Serial(port=com_port, baudrate=baudrate,
                                             parity=parity, stopbits=stopbits,
                                             bytesize=bytesize, timeout=timeout)
        except:
            self.port_status = "open"
            self.close()
            self.serial_port = serial.Serial(port=com_port, baudrate=baudrate,
                                             parity=parity, stopbits=stopbits,
                                             bytesize=bytesize, timeout=timeout)
        self.port_status = "open"

    def open(self):
        if self.port_status == "closed":
            self.serial_port.open()
        elif self.port_status == "open":
            print(self.serial_port.port + " is already open")
        else:
            print("ERROR! unknown COM Port Status")
        self.port_status = "open"

        return

    def close(self):
        if self.port_status == "closed":
            print(self.serial_port.port + " is already closed")
        elif self.port_status == "open":
            self.serial_port.close()
        else:
            print("ERROR! unknown COM Port Status")
        self.port_status = "closed"

        return

    def read_all(self):
        read_buf = self.serial_port.read_all().decode("utf-8", "ignore")

        return read_buf

    def send_cmd(self, command, verbose=True):
        self.serial_port.write((command + '\r\n').encode())
        self.serial_port.flush()
        time.sleep(0.5)

        return self._print_formatted(self.read_all(), verbose)

    def _print_formatted(self, raw_string, verbose=True):
        raw_string_list = raw_string.split("\\r\\n")
        for raw_string_i in range(0, len(raw_string_list)):
            raw_string_list[raw_string_i] = raw_string_list[raw_string_i].replace("\\r",'')
            if verbose == True:
                print(raw_string_list[raw_string_i])

        return raw_string_list
