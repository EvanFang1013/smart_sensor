import serial
#	import pandas as pd
import datetime
import json
from loadparam import parseXML,parseJson
import paho.mqtt.client as mqtt
import time

brokerip, brokertopic,receiveTopic, jsonInformations = parseXML()
tjson = parseJson(jsonInformations[0])

_g_cst_ToMQTTTopicServerIP = brokerip
_g_cst_ToMQTTTopicServerPort = 1883 #port
_g_cst_MQTTTopicName =brokertopic #TOPIC name

# ~ mqttc = mqtt.Client(receiveTopic)
# ~ mqttc.username_pw_set("smgarc1","arc1")
# ~ mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)



port ="/dev/ttyUSB0"
# ~ ser = serial.Serial(port,baudrate=115200)
# ~ ser.timeout = 0.5

def Jsonfmt(jsondata):
	
	tjson.HeaterValue = jsondata
	jsondata= "[%s]"%(tjson.toJSON())

	return jsondata

		
		
# ~ try:
while True:
	# ~ while ser.inWaiting():
	while True:
		# ~ receive = ser.readline().decode()
		# ~ print(receive)
		# ~ data = json.loads(receive)
		data = {"Resistance":"7.055","Temperature":"70.254","healthIndex":"5.040"}
		jsondata=Jsonfmt(data)
		print(jsondata)
		# ~ mqttc.publish(_g_cst_MQTTTopicName,jsondata)
		time.sleep(1)
		

				
# ~ except:
	# ~ print("close")
	# ~ ser.close()
#if __name__ == "__main__":
