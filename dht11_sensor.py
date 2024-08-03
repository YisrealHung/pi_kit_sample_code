import board
import time
import adafruit_dht


dhtDevice = adafruit_dht.DHT11(board.D17)

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
        time.sleep(1)

    except:
        print("temperature can't read")