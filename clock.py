from tkinter import *

from datetime import datetime

import time
import tkinter

def mysleep(s):
    now=time.time()
    while(time.time()-now<s):
        pass

btns = 1
def btn_r_click():
    global btns
    btns = 1
    #print("red"+str(btns))
def btn_sb_click():
    global btns
    btns = 2
    #print("skyblue"+str(btns))
def btn_lg_click():
    global btns
    btns = 3
    #print("lightgreen"+str(btns))
def btn_p_click():
    global btns
    btns = 4
    #print("pink"+str(btns))
def btn_do_click():
    global btns
    btns = 5
    #print("darkorchid"+str(btns))
def btn_go_click():
    global btns
    btns = 6
    #print("gold"+str(btns))
def btn_ora_click():
    global btns
    btns = 7
    #print("darkorange"+str(btns))
def btn_dc_click():
    global btns
    btns = 8
    #print("darkcyan"+str(btns))
def btn_b_click():
    global btns
    btns = 9
    #print("gray"+str(btns))
def btn_w_click():
    global btns
    btns = 10
    #print("white"+str(btns))

root = Tk()
root.iconbitmap('icon.ico')
root.title(u"物語時計")
root.geometry("1000x600")

c = Canvas(root, width = 1000, height = 600, background = 'black')
button_red = tkinter.Button(root, width = 13, height = 5, bg = "red", fg = "white", text="赤齣")
button_skyblue = tkinter.Button(root, width = 13, height = 5, bg = "deepskyblue", fg = "white", text="青齣")   
button_lightgreen = tkinter.Button(root, width = 13, height = 5, bg = "lightgreen", fg = "white", text="緑齣")
button_pink = tkinter.Button(root, width = 13, height = 5, bg = "pink", fg = "white", text="桃齣")
button_darkorchid = tkinter.Button(root, width = 13, height = 5, bg = "darkorchid", fg = "white", text="紫齣")
button_gold = tkinter.Button(root, width = 13, height = 5, bg = "gold", fg = "white", text="黄齣")
button_darkorange = tkinter.Button(root, width = 13, height = 5, bg = "darkorange", fg = "white", text="橙齣")
button_darkcyan = tkinter.Button(root, width = 13, height = 5, bg = "darkcyan", fg = "white", text="碧齣")
button_black = tkinter.Button(root, width = 13, height = 5, bg = "black", fg = "white", text="黒齣")
button_white = tkinter.Button(root, width = 13, height = 5, bg = "white", fg = "gray", text="白齣")

button_red.place(x=0,y=515)
button_skyblue.place(x=100,y=515)
button_lightgreen.place(x=200,y=515)
button_pink.place(x=300,y=515)
button_darkorchid.place(x=400,y=515)
button_gold.place(x=500,y=515)
button_darkorange.place(x=600,y=515)
button_darkcyan.place(x=700,y=515)
button_black.place(x=800,y=515)
button_white.place(x=900,y=515)


button_red["command"] = btn_r_click
button_skyblue["command"] = btn_sb_click
button_lightgreen["command"] = btn_lg_click
button_black["command"] = btn_b_click
button_pink["command"] = btn_p_click
button_darkorchid["command"] = btn_do_click
button_gold["command"] = btn_go_click
button_darkorange["command"] = btn_ora_click
button_darkcyan["command"]= btn_dc_click
button_white["command"]= btn_w_click

c.pack()

#time_list = ["零","壹","貮","參","肆","伍","陸","漆","捌","玖","拾","佰","阡","萬"]
days_dict = {2022:"貮阡貮拾貮",1:"睦月",2:"如月",3:"弥生",4:"卯月",5:"皐月",6:"水無月",7:"文月	",8:"葉月",9:"長月",10:"神無月",11:"霜月",12:"師走"}
time_dict = {0:"零",1:"壹",2:"貮",3:"參",4:"肆",5:"伍",6:"陸",7:"漆",8:"捌",9:"玖",10:"拾",11:"拾壹",12:"拾貮",13:"拾參",14:"拾肆",15:"拾伍",16:"拾陸",17:"拾漆",18:"拾捌",19:"拾玖",20:"貮拾",21:"貮拾壹",22:"貮拾貮",23:"貮拾參",24:"貮拾肆",25:"貮拾伍",26:"貮拾陸",27:"貮拾漆",28:"貮拾捌",29:"貮拾玖",30:"參拾",31:"參拾壹",32:"參拾貮",33:"參拾參",34:"參拾肆",35:"參拾伍",36:"參拾陸",37:"參拾漆",38:"參拾捌",39:"參拾玖",40:"肆拾",41:"肆拾壹",42:"肆拾貮",43:"肆拾參",44:"肆拾肆",45:"肆拾伍",46:"肆拾陸",47:"肆拾漆",48:"肆拾捌",49:"肆拾玖",50:"伍拾",51:"伍拾壹",52:"伍拾貮",53:"伍拾參",54:"伍拾肆",55:"伍拾伍",56:"伍拾陸",57:"伍拾漆",58:"伍拾捌",59:"伍拾玖",60:"零"}

year = ""
month = ""
day = ""
hour = ""
minute = ""
second = ""


try:

    while True:
        
        #print(str(btns))
        now = datetime.now()

        if now.year in days_dict:
            year = days_dict[now.year]

        if now.month in days_dict:
            month = days_dict[now.month]

        if now.day in time_dict:
            day = time_dict[now.day]

        if now.hour in time_dict:
            hour = time_dict[now.hour]

        if now.minute in time_dict:
            minute = time_dict[now.minute]      
        
        if now.second in time_dict:
            second = time_dict[now.second]

        if btns == 1:
            bgcolor = 'red'
            fcolor = "white"
            coma = "赤齣"
            color = "aka."
        elif btns == 2:
            bgcolor = 'deepskyblue'
            fcolor = "white"
            coma = "青齣"
            color = "ao."
        elif btns == 3:
            bgcolor = 'lightgreen'
            fcolor = "white"
            coma = "緑齣"
            color = "midori."
        elif btns == 4:
            bgcolor = "pink"
            fcolor = "white"
            coma = "桃齣"
            color = "momo."
        elif btns == 5:
            bgcolor = "darkorchid"
            fcolor = "white"
            coma = "紫齣"
            color = "murasaki."
        elif btns == 6:
            bgcolor = "gold"
            fcolor = "white"
            coma = "黄齣"
            color = "ki."
        elif btns == 7:
            bgcolor = "darkorange"
            fcolor = "white"
            coma = "橙齣"
            color = "daidai."
        elif btns == 8:
            bgcolor = "darkcyan"
            fcolor = "white"
            coma = "碧齣"
            color = "ao. midori."
        elif btns == 9:
            bgcolor = "black"
            fcolor = "white"
            coma = "黒齣"
            color = "kuro."
        elif btns == 10:
            bgcolor = "white"
            fcolor = "black"
            coma = "白齣"
            color = "shiro."
        else:
            bgcolor = "black"
            fcolor = "white"
            coma = "エラー"
            color = "error"
        #s = '{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second)
        s = '{0}時 {1}分 {2}秒'.format(hour, minute, second)
        t = coma
        u = '({0}年 {1}月 {2}日 {3:0>2d}:{4:0>2d}:{5:0>2d})'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        v = '動畫番號 無シ'
        w = color
        x = '{0}年  {1}  {2}日'.format(year, month, day)

        c.create_rectangle(0, 0, 1000, 600, outline = 'black', fill = bgcolor)

        c.create_text(500, 270, text = s, font = ('游明朝', 55), fill = fcolor)
        c.create_text(500, 80, text = t, font = ('游明朝', 65), fill = fcolor)
        c.create_text(500, 370, text = u, font = ('游明朝', 25), fill = fcolor)
        c.create_text(500, 475, text = v, font = ('游明朝', 25), fill = fcolor)
        c.create_text(500, 330, text = w, font = ('Mongolian Baiti', 25), fill = fcolor)
        c.create_text(500, 180, text = x, font = ('游明朝', 40), fill = fcolor)

        c.update()

        a = mysleep(0.1)
except:

    pass