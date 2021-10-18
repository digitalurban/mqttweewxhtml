import json
import paho.mqtt.client as mqtt
import time



# MQTT

print("creating new instance")
client = mqtt.Client("P1") #  create new instance
print("connecting to broker")
client.username_pw_set("YourUsername", "YourPassword")
client.connect("YourMQTTServer", YourMQTTPort) #  connect to broker



with open('weewx.json') as f:
  data = (json.load(f))
  tempmax = round((data['day']['max temperature']['value']),1)
  tempmin = round((data['day']['min temperature']['value']),1)
  pressuremax = round((data['day']['max barometer']['value']),1)
  pressuremin = round((data['day']['min barometer']['value']),1)
  windmaxkm = round((data['day']['max wind gust']['value']),1)
  windmax = round((windmaxkm*0.6213711922),1)
  barotrend = round((data['current']['baro trend']['value']),1)
  temptrend = round((data['current']['temp trend']['value']),1)




print(tempmax)
print(tempmin)
print(pressuremax)
print(pressuremin)
print(windmax)
print(barotrend)
print(temptrend)

client.publish("weather/tempmin", tempmin, retain=True)
client.publish("weather/tempmax", tempmax, retain=True)
client.publish("weather/pressuremin", pressuremin, retain=True)
client.publish("weather/pressuremax", pressuremax, retain=True)
client.publish("weather/pressuretrend", barotrend, retain=True)
client.publish("weather/windmax", windmax, retain=True)
client.publish("weather/barotrend", barotrend, retain=True)
client.publish("weather/temptrend", temptrend, retain=True)
