from lxml import etree
import json
import paho.mqtt.client as mqtt
import time 

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        

def parseXML():
   with open('BaseConfig.xml') as data:
       xslt_content = data.read()
       #~ print(xslt_content)
   
   xslt_content = xslt_content.encode('utf-8')
   root = etree.fromstring(xslt_content)
   xmllistprop = []
   jsonInformations = []
   brokerip = root[5].text
   print("IP",brokerip)
   brokertopic = root[6].text
   print("TOPIC",brokertopic)
   receiveTopic = root[7].text
   # ~ print(receiveTopic)
   for appt in root.getchildren():
       # ~ print(appt.tag)
       for elem in appt.getchildren():
           xmllistprop.append(elem.text)
           
       if(len(xmllistprop) != 0):          
           jsonInformations.append(xmllistprop)
           print(jsonInformations)
       xmllistprop= []      
           

   return brokerip, brokertopic,receiveTopic, jsonInformations
       
def parseJson(ALLJSON):

    tf = Object()
       
    tf.Module = ALLJSON[0]
    tf.MachineName = ALLJSON[1]
    tf.MachineId = ALLJSON[2]
    tf.HeaterValue = Object()
    return tf

                
                 

            
          



