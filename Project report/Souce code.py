import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "kz2her"
deviceType = "NODE"
deviceId = "4222"
authMethod = "token"
authToken = " j5RIM+NYy8Uv6+!s4q"
# Initialize GPIO
try:
  deviceOptions = {"org": organization, "type": deviceType, "id":
  deviceId, "auth-method": authMethod, "auth-token": authToken}
  deviceCli = ibmiotf.device.Client(deviceOptions)
#..............................................
except Exception as e:
  print("Caught exception connecting device: %s" % str(e))
  sys.exit()
# Connect and send a datapoint "hello" with value "world" into the cloud asan event of type "greeting" 10 times

deviceCli.connect()
while True:
 #Get Sensor Data from DHT11

  Propane = random.randint(0, 500);
  Carbon_Monoxide = random.randint(0, 500);
  LPG= random.randint(0, 1000);
  Methane = random.randint(0, 500);
  Hydrogen= random.randint(0, 500);
  Temperature=random.randint(0,100 );
  Humidity=random.randint(0,100 );


  data = { "temp" : Temperature, "Humid": Humidity,"Propane": Propane,
 "Carbon_Monoxide": Carbon_Monoxide,
 "LPG": LPG,
 "Methane": Methane,
 "Hydrogen":Hydrogen  }
 #print data
  def myOnPublishCallback():
    print ("Published Temperature = %s C" % Temperature, "Humidity = %s%%" % Humidity,"Propane = %s ppm" % Propane, "LPG = %s ppm" % LPG,"Methane = %s ppm" % Methane,"Hydrogen = %s ppm" % Hydrogen,"Carbon monoxide = %s ppm" % Carbon_Monoxide , "to IBM Watson")
    if (Propane or Carbon_Monoxide or LPG or Methane or Hydrogen)>150:
     print("GAS LEAKAGE FOUND")
    else:
     print("NO LEAKAGE")
     

  success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0,on_publish=myOnPublishCallback)
    
  if not success:
    print("Not connected to IoTF")
  time.sleep(10)

  deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
