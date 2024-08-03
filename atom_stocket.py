import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

def data_parse():
    volt = 0
    curr = 0.0
    power = 0
    while True:
        data = ser.readline().decode('utf-8').rstrip()
        if ("Voltage" in data):
            volt = int(data.split(" ")[1])
            data = ser.readline().decode('utf-8').rstrip()
            curr = float(data.split(" ")[1])
            data = ser.readline().decode('utf-8').rstrip()
            power = int(data.split(" ")[1])
            break
    return volt, curr, power


while True:
    Voltage, Current, ActivePower = data_parse()

    print("Voltage: {}, Current: {}, ActivePower: {}".format(Voltage, Current, ActivePower))
