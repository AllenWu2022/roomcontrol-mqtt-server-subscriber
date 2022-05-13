import paho.mqtt.client as mqtt
import time
import json
import random
#變數設定
MQTT_TOPIC = "boboray"  
MQTT_SERVER = "127.0.0.1"  
MQTT_PORT = 1883  
MQTT_ALIVE = 60  

#------------
#mqtt client 物件
mqtt_client=mqtt.Client()
#連線MQTT Server
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)

while True:
    temp=random.randint(0,30)
    payload={
        "Topic":MQTT_TOPIC,
        "溫度":temp
    }
    print("目標 topic:"+MQTT_TOPIC+"=>溫度:"+str(temp))
    #送出topic訊息，須加入ensure_ascii=False讓中文正常顯示
    mqtt_client.publish(MQTT_TOPIC, json.dumps(payload, ensure_ascii=False),qos=1)
    time.sleep(10) 