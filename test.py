from datetime import datetime

import time

time_list = ["零","壹","貮","參","肆","伍","陸","漆","捌","玖","拾","佰","阡","萬"]
#print(time_list[10]+time_list[1])
hour = ""
minute = ""
second = ""

while True:
    now = datetime.now()
    if now.hour == 0:
        hour = time_list[0]
    elif now.hour == 1:
        hour = time_list[1]
    elif now.hour == 2:
        hour = time_list[2]
    elif now.hour == 3:
        hour = time_list[3]
    elif now.hour == 4:
        hour = time_list[4]
    elif now.hour == 5:
        hour = time_list[5]
    elif now.hour == 6:
        hour = time_list[6]
    elif now.hour == 7:
        hour = time_list[7]
    elif now.hour == 8:
        hour = time_list[8]
    elif now.hour == 9:
        hour = time_list[9]
    elif now.hour == 10:
        hour = time_list[10]
    elif now.hour == 11:
        hour = time_list[10]+time_list[1]
    elif now.hour == 12:
        hour = time_list[10]+time_list[2]
    elif now.hour == 13:
        hour = time_list[10]+time_list[3]
    elif now.hour == 14:
        hour = time_list[10]+time_list[4]
    elif now.hour == 15:
        hour = time_list[10]+time_list[5]
    elif now.hour == 16:
        hour = time_list[10]+time_list[6]
    elif now.hour == 17:
        hour = time_list[10]+time_list[7]
    elif now.hour == 18:
        hour = time_list[10]+time_list[8]
    elif now.hour == 19:
        hour = time_list[10]+time_list[9]
    elif now.hour == 20:
        hour = time_list[2]+time_list[10]
    elif now.hour == 21:
        hour = time_list[2]+time_list[10]+time_list[1]
    elif now.hour == 22:
        hour = time_list[2]+time_list[10]+time_list[2]
    elif now.hour == 23:
        hour = time_list[2]+time_list[10]+time_list[3]
    elif now.hour == 24:
        hour = time_list[2]+time_list[10]+time_list[4] 

    if now.minute == 0:
        minute = time_list[0]
    elif now.minute == 1:
        minute = time_list[1]
    elif now.minute == 2:
        minute = time_list[2]
    elif now.minute == 3:
        minute = time_list[3]
    elif now.minute == 4:
        minute = time_list[4]
    elif now.minute == 5:
        minute = time_list[5]
    elif now.minute == 6:
        minute = time_list[6]
    elif now.minute == 7:
        minute = time_list[7]
    elif now.minute == 8:
        minute = time_list[8]
    elif now.minute == 9:
        minute = time_list[9]
    elif now.minute == 10:
        minute = time_list[10]
    elif now.minute == 11:
        minute = time_list[10]+time_list[1]
    elif now.minute == 12:
        minute = time_list[10]+time_list[2]
    elif now.minute == 13:
        minute = time_list[10]+time_list[3]
    elif now.minute == 14:
        minute = time_list[10]+time_list[4]
    elif now.minute == 15:
        minute = time_list[10]+time_list[5]
    elif now.minute == 16:
        minute = time_list[10]+time_list[6]
    elif now.minute == 17:
        minute = time_list[10]+time_list[7]
    elif now.minute == 18:
        minute = time_list[10]+time_list[8]
    elif now.minute == 19:
        minute = time_list[10]+time_list[9]
    elif now.minute == 20:
        minute = time_list[2]+time_list[10]
    elif now.minute == 21:
        minute = time_list[2]+time_list[10]+time_list[1]
    elif now.minute == 22:
        minute = time_list[2]+time_list[10]+time_list[2]
    elif now.minute == 23:
        minute = time_list[2]+time_list[10]+time_list[3]
    elif now.minute == 24:
        minute = time_list[2]+time_list[10]+time_list[4]
    elif now.minute == 25:
        minute = time_list[2]+time_list[10]+time_list[5]
    elif now.minute == 26:
        minute = time_list[2]+time_list[10]+time_list[6]
    elif now.minute == 27:
        minute = time_list[2]+time_list[10]+time_list[7]
    elif now.minute == 28:
        minute = time_list[2]+time_list[10]+time_list[8]
    elif now.minute == 29:
        minute = time_list[2]+time_list[10]+time_list[9]
    elif now.minute == 30:
        minute = time_list[3]+time_list[10]
    elif now.minute == 31:
        minute = time_list[3]+time_list[10]+time_list[1]
    elif now.minute == 32:
        minute = time_list[3]+time_list[10]+time_list[2]
    elif now.minute == 33:
        minute = time_list[3]+time_list[10]+time_list[3]
    elif now.minute == 34:
        minute = time_list[3]+time_list[10]+time_list[4]
    elif now.minute == 35:
        minute = time_list[3]+time_list[10]+time_list[5]
    elif now.minute == 36:
        minute = time_list[3]+time_list[10]+time_list[6]
    elif now.minute == 37:
        minute = time_list[3]+time_list[10]+time_list[7]
    elif now.minute == 38:
        minute = time_list[3]+time_list[10]+time_list[8]
    elif now.minute == 39:
        minute = time_list[3]+time_list[10]+time_list[9]
    elif now.minute == 40:
        minute = time_list[4]+time_list[10]
    elif now.minute == 41:
        minute = time_list[4]+time_list[10]+time_list[1]
    elif now.minute == 42:
        minute = time_list[4]+time_list[10]+time_list[2]
    elif now.minute == 43:
        minute = time_list[4]+time_list[10]+time_list[3]
    elif now.minute == 44:
        minute = time_list[4]+time_list[10]+time_list[4]
    elif now.minute == 45:
        minute = time_list[4]+time_list[10]+time_list[5]
    elif now.minute == 46:
        minute = time_list[4]+time_list[10]+time_list[6]
    elif now.minute == 47:
        minute = time_list[4]+time_list[10]+time_list[7]
    elif now.minute == 48:
        minute = time_list[4]+time_list[10]+time_list[8]
    elif now.minute == 49:
        minute = time_list[4]+time_list[10]+time_list[9]
    elif now.minute == 50:
        minute = time_list[5]+time_list[10]
    elif now.minute == 51:
        minute = time_list[5]+time_list[10]+time_list[1]
    elif now.minute == 52:
        minute = time_list[5]+time_list[10]+time_list[2]
    elif now.minute == 53:
        minute = time_list[5]+time_list[10]+time_list[3]
    elif now.minute == 54:
        minute = time_list[5]+time_list[10]+time_list[4]
    elif now.minute == 55:
        minute = time_list[5]+time_list[10]+time_list[5]
    elif now.minute == 56:
        minute = time_list[5]+time_list[10]+time_list[6]
    elif now.minute == 57:
        minute = time_list[5]+time_list[10]+time_list[7]
    elif now.minute == 58:
        minute = time_list[5]+time_list[10]+time_list[8]
    elif now.minute == 59:
        minute = time_list[5]+time_list[10]+time_list[9]

    if now.second == 0:
        second = time_list[0]
    elif now.second == 1:
        second = time_list[1]
    elif now.second == 2:
        second = time_list[2]
    elif now.second == 3:
        second = time_list[3]
    elif now.second == 4:
        second = time_list[4]
    elif now.second == 5:
        second = time_list[5]
    elif now.second == 6:
        second = time_list[6]
    elif now.second == 7:
        second = time_list[7]
    elif now.second == 8:
        second = time_list[8]
    elif now.second == 9:
        second = time_list[9]
    elif now.second == 10:
        second = time_list[10]
    elif now.second == 11:
        second = time_list[10]+time_list[1]
    elif now.second == 12:
        second = time_list[10]+time_list[2]
    elif now.second == 13:
        second = time_list[10]+time_list[3]
    elif now.second == 14:
        second = time_list[10]+time_list[4]
    elif now.second == 15:
        second = time_list[10]+time_list[5]
    elif now.second == 16:
        second = time_list[10]+time_list[6]
    elif now.second == 17:
        second = time_list[10]+time_list[7]
    elif now.second == 18:
        second = time_list[10]+time_list[8]
    elif now.second == 19:
        second = time_list[10]+time_list[9]
    elif now.second == 20:
        second = time_list[2]+time_list[10]
    elif now.second == 21:
        second = time_list[2]+time_list[10]+time_list[1]
    elif now.second == 22:
        second = time_list[2]+time_list[10]+time_list[2]
    elif now.second == 23:
        second = time_list[2]+time_list[10]+time_list[3]
    elif now.second == 24:
        second = time_list[2]+time_list[10]+time_list[4]
    elif now.second == 25:
        second = time_list[2]+time_list[10]+time_list[5]
    elif now.second == 26:
        second = time_list[2]+time_list[10]+time_list[6]
    elif now.second == 27:
        second = time_list[2]+time_list[10]+time_list[7]
    elif now.second == 28:
        second = time_list[2]+time_list[10]+time_list[8]
    elif now.second == 29:
        second = time_list[2]+time_list[10]+time_list[9]
    elif now.second == 30:
        second = time_list[3]+time_list[10]
    elif now.second == 31:
        second = time_list[3]+time_list[10]+time_list[1]
    elif now.second == 32:
        second = time_list[3]+time_list[10]+time_list[2]
    elif now.second == 33:
        second = time_list[3]+time_list[10]+time_list[3]
    elif now.second == 34:
        second = time_list[3]+time_list[10]+time_list[4]
    elif now.second == 35:
        second = time_list[3]+time_list[10]+time_list[5]
    elif now.second == 36:
        second = time_list[3]+time_list[10]+time_list[6]
    elif now.second == 37:
        second = time_list[3]+time_list[10]+time_list[7]
    elif now.second == 38:
        second = time_list[3]+time_list[10]+time_list[8]
    elif now.second == 39:
        second = time_list[3]+time_list[10]+time_list[9]
    elif now.second == 40:
        second = time_list[4]+time_list[10]
    elif now.second == 41:
        second = time_list[4]+time_list[10]+time_list[1]
    elif now.second == 42:
        second = time_list[4]+time_list[10]+time_list[2]
    elif now.second == 43:
        second = time_list[4]+time_list[10]+time_list[3]
    elif now.second == 44:
        second = time_list[4]+time_list[10]+time_list[4]
    elif now.second == 45:
        second = time_list[4]+time_list[10]+time_list[5]
    elif now.second == 46:
        second = time_list[4]+time_list[10]+time_list[6]
    elif now.second == 47:
        second = time_list[4]+time_list[10]+time_list[7]
    elif now.second == 48:
        second = time_list[4]+time_list[10]+time_list[8]
    elif now.second == 49:
        second = time_list[4]+time_list[10]+time_list[9]
    elif now.second == 50:
        second = time_list[5]+time_list[10]
    elif now.second == 51:
        second = time_list[5]+time_list[10]+time_list[1]
    elif now.second == 52:
        second = time_list[5]+time_list[10]+time_list[2]
    elif now.second == 53:
        second = time_list[5]+time_list[10]+time_list[3]
    elif now.second == 54:
        second = time_list[5]+time_list[10]+time_list[4]
    elif now.second == 55:
        second = time_list[5]+time_list[10]+time_list[5]
    elif now.second == 56:
        second = time_list[5]+time_list[10]+time_list[6]
    elif now.second == 57:
        second = time_list[5]+time_list[10]+time_list[7]
    elif now.second == 58:
        second = time_list[5]+time_list[10]+time_list[8]
    elif now.second == 59:
        second = time_list[5]+time_list[10]+time_list[9]


    print('{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second))
    print('{0}:{1}:{2}'.format(hour, minute, second))
    time.sleep(1.0)
