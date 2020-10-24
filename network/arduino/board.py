import serial


class Arduino_UNO:
    board_name = 'Arduino UNO'
    digital_pin_num = 14
    analog_pin_num = 6
    
    def __init__(self, port=None, baud=38400):
        self.port = port
        self.baud = baud
        self.comm = serial.Serial(port, baud)

    def send_cmd(self, command, params):
        
        self.comm.write(('{%s%s}' % (command, params)).encode())
        self.comm.flush()
        
        # self.comm.readline()
        
    def digitalWrite(self, pin, value):
        if pin >= self.digital_pin_num:
            print('WARNING: Invalid pin number!\n There are only %d digital pins on %s.' % (self.digital_pin_num, self.board_name))
        pin = str(pin).zfill(2)
        value = 'H' if value else 'L'
        self.send_cmd('dW', pin + value)

    def analogWrite(self, pin, value):
        if pin not in [3, 5, 6, 9, 10, 11]:
            print('WARNING: Invalid pin number!\n pin #%d on %s does not have PWM function.' % (pin, self.board_name))
        pin = str(pin).zfill(2)
        value = str(min(max(value, 0), 255))
        value = value.zfill(3)
        self.send_cmd('aW', pin + value)
    
    def servoWrite(self, pin, angle):
        pin = str(pin).zfill(2)
        angle = str(min(max(angle, 0), 180))
        self.send_cmd('Sv', pin + angle)

    def EMERGENCYSTOP(self):
        self.comm.write(b'{!!}')
        print('WARNING: %s has stopped due to an EMERGENCYSTOP.' % self.board_name)


