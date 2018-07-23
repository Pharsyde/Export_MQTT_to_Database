import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
#        printLine()
#        printMsg("Address:\t ] %s" % (broker_address))
#        printMsg("Port:\t\t ] %s" % (broker_port))
#        printMsg("Username:\t ] %s" % (sUsername))
#        printMsg("Connected to server")
#        printLine()
    else:
    	print("Connection failed. rc= "+str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print("Message received on topic "+msg.topic + " with QoS " + str(msg.qos) + " and payload " + str(msg.payload))

#def on_message(client, userdata, message):
#    print("message received " ,str(message.payload.decode("utf-8")))
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)

def on_log(client, userdata, level, string):
    print(string)

broker_address=''
broker_port='1883'
topic='#'
client_id='dbexport'
keep_alive_interval = 45
mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log

# Connect
#mqttc.username_pw_set(UserName, Password)
mqttc.connect(broker_address, broker_port, int(keep_alive_interval))

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

mqttc.loop_forever()

#rc = 0
#while rc == 0:
#    rc = mqttc.loop()
#print("rc: " + str(rc))


#client.loop_start()
#mqttc.subscribe(topic, 0)
#time.sleep(4)
#client.loop_stop()
