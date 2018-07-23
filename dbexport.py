import paho.mqtt.client as mqtt
import time
import sqlite3

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
#        print("[Address:\t ] %s" % (broker_address))
#        print("[Port:\t\t ] %s" % (broker_port))
#        print("[Username:\t ] %s" % (UserName))
#        print("[Status:\t] Connected to server")
    else:
    	print("Connection failed. rc= "+str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
#    print("Message received on topic "+msg.topic + " with QoS " + str(msg.qos) + " and payload " + str(msg.payload))
    print('[Topic:\t\t] %s' % (msg.topic))
    print('[QoS:\t\t] %s' % (str(msg.qos)))
    print('[Data:\t\t] %s' % (str(msg.payload.decode("utf-8"))))
    print('[Retain flag:\t] %s' % (msg.retain))
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute('insert into messages (topic, message) values (?, ?)', [msg.topic, msg.payload])
    conn.commit()
    curs.close()
    conn.close()

def on_log(client, userdata, level, string):
    print(string)

broker_address='91.238.227.244'
broker_port='1883'
topic='#'
client_id='dbexport'
keep_alive_interval = 45
dbname='sem365.db'
mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log

# Connect
#mqttc.username_pw_set(UserName, Password)
mqttc.connect(broker_address, broker_port, int(keep_alive_interval))

client.loop_start()
# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

#mqttc.loop_forever()

#rc = 0
#while rc == 0:
#    rc = mqttc.loop()
#print("rc: " + str(rc))

#mqttc.subscribe(topic, 0)
time.sleep(10)
client.loop_stop()
