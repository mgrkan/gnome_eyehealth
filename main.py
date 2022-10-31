#!/usr/bin/env python3
import time
from face_detection import distance
from gi import require_version
require_version('Notify', '0.7')
from gi.repository import Notify

def distance_noti(d):
    
    if d < 48:
        summary = "You are too close: " + str(int(d)) +  " cm"
        body = "Get a little further from the screen"
        notification = Notify.Notification.new(summary, body)
        notification.show()
        time.sleep(6)
        notification.clear_actions()
        notification.close()

def time_noti():
    summary = "It's been 20 minutes..."
    body = "You should get away from the screen for some time"
    notification = Notify.Notification.new(summary, body)
    print("20 minutes passed")
    notification.show()
    time.sleep(30)
    notification.close()
    
Notify.init("Eyesight Health")
dstart_time = int(time.time())
tstart_time = int(time.time())
while True:

    if int(time.time()) == dstart_time + 180:
        dstart_time = int(time.time())
        print(dstart_time)
        distance_noti(distance())
    elif int(time.time()) == tstart_time + 1200:
        tstart_time = int(time.time())
        time_noti()
