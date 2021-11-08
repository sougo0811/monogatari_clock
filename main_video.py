from tkinter import *

from datetime import datetime

import time


root = Tk()
root.title(u"物語時計")
root.geometry("3440x1440")

c = Canvas(root, width = 3440, height = 1440, background = 'red')

c.pack()

#time_list = ["零","壹","貮","參","肆","伍","陸","漆","捌","玖","拾","佰","阡","萬"]
time_dict = {0:"零",1:"壹",2:"貮",3:"參",4:"肆",5:"伍",6:"陸",7:"漆",8:"捌",9:"玖",10:"拾",11:"拾壹",12:"拾貮",13:"拾參",14:"拾肆",15:"拾伍",16:"拾陸",17:"拾漆",18:"拾捌",19:"拾玖",20:"貮拾",21:"貮拾壹",22:"貮拾貮",23:"貮拾參",24:"貮拾肆",25:"貮拾伍",26:"貮拾陸",27:"貮拾漆",28:"貮拾捌",29:"貮拾玖",30:"參拾",31:"參拾壹",32:"參拾貮",33:"參拾參",34:"參拾肆",35:"參拾伍",36:"參拾陸",37:"參拾漆",38:"參拾捌",39:"參拾玖",40:"肆拾",41:"肆拾壹",42:"肆拾貮",43:"肆拾參",44:"肆拾肆",45:"肆拾伍",46:"肆拾陸",47:"肆拾漆",48:"肆拾捌",49:"肆拾玖",50:"伍拾",51:"伍拾壹",52:"伍拾貮",53:"伍拾參",54:"伍拾肆",55:"伍拾伍",56:"伍拾陸",57:"伍拾漆",58:"伍拾捌",59:"伍拾玖",60:"零"}

hour = ""
minute = ""
second = ""


try:

    while True:

        now = datetime.now()

        if now.hour in time_dict:
            hour = time_dict[now.hour]

        if now.minute in time_dict:
            minute = time_dict[now.minute]      
        
        if now.second in time_dict:
            second = time_dict[now.second]

        #s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
        s = '{0}時 {1}分 {2}秒'.format(hour, minute, second)
        t = '赤齣'
        u = '({0:0>2d}:{1:0>2d}:{2:0>2d})'.format(now.hour, now.minute, now.second)
        v = '動畫番號 無シ'
        w = 'aka.'

        c.create_rectangle(0, 0, 3440, 1440, outline = 'red', fill = 'red')

        c.create_text(1720, 650, text = s, font = ('游明朝', 120), fill = 'white')
        c.create_text(1720, 250, text = t, font = ('游明朝', 150), fill = 'white')
        c.create_text(1720, 900, text = u, font = ('游明朝', 65), fill = 'white')
        c.create_text(1720, 1200, text = v, font = ('游明朝', 65), fill = 'white')
        c.create_text(1720, 800, text = w, font = ('Mongolian Baiti', 45), fill = 'white')

        c.update()

        time.sleep(0.1)
except:

    pass