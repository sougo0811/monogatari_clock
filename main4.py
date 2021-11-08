from tkinter import *  #Window表示
from datetime import datetime  #日時を取得

import time  #sleepで0.1秒毎に表示を切り替える
import math  #三角関数・円周率

WINwidth = 300  #時計の大きさ（min=200:変更箇所はここだけ）
WINcolor = 'deepskyblue'  #BackGroundColor

WINheight = WINwidth  #Windowの高さ
S_length = WINwidth / 2 * 0.75  #秒針長さ
M_length = S_length * 0.95  #分針長さ
H_length = S_length * 0.8  #時針長さ
H_LINEwidth = 8  #時針の太さ
M_LINEwidth = H_LINEwidth / 2  #分針の太さ
S_LINEwidth = 1  #秒針の太さ

#Windowを作成
Clock = Tk()
Clock.title("物語時計var AD")

w = Canvas(Clock, width = WINwidth, height = WINheight, background = WINcolor)
w.pack()

w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill = 'white')  #中心●
w.create_oval(5, 5, WINwidth-5, WINheight-5, width = 2, outline="white")  #時計の外形円

FontSize = int(WINwidth / 20)  #時間文字のサイズ
Fx = 0  #時間文字の位置を修正
Fy = FontSize / 10
R = S_length + FontSize * 0.9  #時間文字位置の半径
A = 0  #時間文字位置の角度
clocks = ["壹","貮","參","肆","伍","陸","漆","捌","玖","拾","拾壹","拾貮"]
for i in clocks:  #文字盤表示
    A = A + 30
    Tx = R * math.cos(A / 180 * math.pi)  #時間文字の座標
    Ty = R * math.sin(A / 180 * math.pi)
    w.create_text(WINwidth / 2 + Ty - Fx, WINheight / 2 - Tx + Fy, text = "\n".join(i), font = ("Times", FontSize), fill = 'white')

days_dict = {2021:"貮阡貮拾壹",1:"睦月",2:"如月",3:"弥生",4:"卯月",5:"皐月",6:"水無月",7:"文月	",8:"葉月",9:"長月",10:"神無月",11:"霜月",12:"師走"}
time_dict = {0:"零",1:"壹",2:"貮",3:"參",4:"肆",5:"伍",6:"陸",7:"漆",8:"捌",9:"玖",10:"拾",11:"拾壹",12:"拾貮",13:"拾參",14:"拾肆",15:"拾伍",16:"拾陸",17:"拾漆",18:"拾捌",19:"拾玖",20:"貮拾",21:"貮拾壹",22:"貮拾貮",23:"貮拾參",24:"貮拾肆",25:"貮拾伍",26:"貮拾陸",27:"貮拾漆",28:"貮拾捌",29:"貮拾玖",30:"參拾",31:"參拾壹",32:"參拾貮",33:"參拾參",34:"參拾肆",35:"參拾伍",36:"參拾陸",37:"參拾漆",38:"參拾捌",39:"參拾玖",40:"肆拾",41:"肆拾壹",42:"肆拾貮",43:"肆拾參",44:"肆拾肆",45:"肆拾伍",46:"肆拾陸",47:"肆拾漆",48:"肆拾捌",49:"肆拾玖",50:"伍拾",51:"伍拾壹",52:"伍拾貮",53:"伍拾參",54:"伍拾肆",55:"伍拾伍",56:"伍拾陸",57:"伍拾漆",58:"伍拾捌",59:"伍拾玖",60:"零"}

year = ""
month = ""
day = ""
hour = ""
minute = ""
second = ""

try:
    while True:
        #ここから無限ループ
        now = datetime.now()  #現在の時間を取得
        if now.hour > 12:  #12時間表示
            nowhour = now.hour - 12
        else:
            nowhour = now.hour
        #秒針が動くと時分針も動かす
        nowhour = nowhour + now.minute / 60 + now.second / 3600  #時間を時に変換：例．1時30分30秒ー＞1.5083・・・
        nowminute = now.minute + now.second / 60  #分秒を分に変換

        H_A = nowhour / 12 * 360 * math.pi /180  #針の角度
        M_A = nowminute / 60 * 360 * math.pi / 180
        S_A = now.second / 60 * 360 * math.pi / 180

        H_x = math.cos(H_A) * H_length  #針の先端の座標計算（中心基準）
        H_y = math.sin(H_A) * H_length
        M_x = math.cos(M_A) * M_length
        M_y = math.sin(M_A) * M_length
        S_x = math.cos(S_A) * S_length
        S_y = math.sin(S_A) * S_length

        #w.create_text(WINwidth / 2 , WINheight / 2 + WINwidth / 8, text = datetime.now().strftime('%Y/%m/%d %H:%M:%S'), font = ("", int(FontSize / 1.5)), tag="Y", fill = 'white')  #年月日時分秒
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

        S = '{0}時 {1}分 {2}秒'.format(hour, minute, second)
        T = '{0}年  {1}  {2}日'.format(year, month, day)
        w.create_text(WINwidth / 2 , WINheight / 2 + WINwidth / 6, text = S, font = ("游明朝", int(FontSize / 2)), tag="Y", fill = 'white')
        w.create_text(WINwidth / 2 , WINheight / 2 + WINwidth / 12, text = T, font = ("游明朝", int(FontSize / 2)), tag="Y", fill = 'white')

        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width = H_LINEwidth, tag="H", fill = 'white') #時針
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width = M_LINEwidth, tag="M", fill = 'white') #分針
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width = S_LINEwidth, tag="S", fill = 'white') #秒針

        w.update()  #新しい針とカレンダーを表示

        w.delete("H")  #針とカレンダーを消去
        w.delete("M")
        w.delete("S")
        w.delete("Y")

        time.sleep(0.1)  #0.1秒毎に描画
except:

    pass