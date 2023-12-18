# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:15:35 2023

@author: Ferdinand
"""

import json
import requests
import time
import paho.mqtt.client as mqtt
from requests.exceptions import HTTPError

#Define input variables
# Provide IP-address of UMR2
UMR2_IP = "192.168.2.138"
# Interval for UMR2 polling in seconds
timesleep = 10
# Define MQTT parameters
MQTT_HOST = "192.168.2.31"
MQTT_PORT = 1883
MQTT_TOPIC = "Vloerverwarming"

#Define derived variables
UMR2_URL = "http://" + UMR2_IP + "/get.json?f=$.status.*"
MQTT_KEEPALIVE_INTERVAL = 3 * timesleep

def main():
	mqttc = mqtt.Client()
	mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
	mqttc.loop_start()
	while True:
		try:
		    response = requests.get(UMR2_URL)
		    jsonResponse = response.json()
		except HTTPError as http_err:
		    response=""
		except Exception as err:
		    response=""
		if response != "":
		    mode = str(jsonResponse['status']['outputs']['heater']['mode'])
		    pump = int(jsonResponse['status']['outputs']['pump']['speed'])
		    valve = int(jsonResponse['status']['outputs']['valves'][8]['state'])
		    Tsupply = jsonResponse['status']['inputs']['max']['temperature']
		    Treturn = jsonResponse['status']['inputs']['return']['temperature']
		    DeltaT = float(Tsupply) - float(Treturn)
		    MQTT_MSG = json.dumps({"Mode": mode,"Pomp": pump,"Klep": valve,"Tsupply": Tsupply,"Treturn": Treturn,"DeltaT": DeltaT});
		    mqttc.publish(MQTT_TOPIC, MQTT_MSG)
		time.sleep(timesleep)

if __name__ == '__main__':
    main()