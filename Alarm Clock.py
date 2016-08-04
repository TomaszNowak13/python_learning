"""A simple clock where it plays a sound at a particular time."""

import winsound
import datetime

def alarm():
    notification = input("Please set your notification: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now1 = datetime.datetime.now()
    print("\nCurrent time: ", now)
    print("\nSet the alarm clock: ")
    hour = int(input("Hour: "))
    minute = int(input("Minute: "))
    second = int(input("Second: "))
    if hour <= now1.hour and minute <= now1.minute and second <= now1.second:
        alarm_time = datetime.datetime(now1.year, now1.month, now1.day + 1, hour, minute, second).strftime("%Y-%m-%d %H:%M:%S")
    else:
        alarm_time = datetime.datetime(now1.year, now1.month, now1.day, hour, minute, second).strftime("%Y-%m-%d %H:%M:%S")
    print ("\nAlarm time: ", alarm_time)

    while alarm_time != now:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(notification)
    return winsound.Beep(2600,1000)

alarm()
