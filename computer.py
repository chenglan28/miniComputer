from machine import Timer
from mpython import *
import framebuf
import font.digiface_11
import time
import network
import ntptime
import music
clock = Clock(oled, 15, 15, 15)
#定义时钟
def display_font(_font, _str, _x, _y, _wrap, _z=0):
    _start = _x
    for _c in _str:
        _d = _font.get_ch(_c)
        if _wrap and _x > 128 - _d[2]: _x = _start; _y += _d[1]
        if _c == '1' and _z > 0: oled.fill_rect(_x, _y, _d[2], _d[1], 0)
        oled.blit(framebuf.FrameBuffer(bytearray(_d[0]), _d[2], _d[1],
        framebuf.MONO_HLSB), (_x+int(_d[2]/_z)) if _c=='1' and _z>0 else _x, _y)
        _x += _d[2]
time.localtime()[0]
# 数码管字体
wifi = wifi()
# 网络
# 引用库

inputCharacter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '`', '-', '=', '{', '}', '|', ':', '"', '<', '>', '?', '[', ']', '\\', ';', "'", ',', '.', '/', ' ', 'Del', 'Get', 'Clock']
# 所有字符
inputChoice = ""
# 选择的字符
cmd = ""
# 命令

oled.fill(0)
oled.DispChar("miniComputer 1.3", 0, 0, 1)
oled.show()
# 重启刷新

def timer1_tick(_):
    oled.fill_rect(0, 0, 128, 32, 0)
    display_font(font.digiface_11, str(time.localtime()[0]) + "/" + str(time.localtime()[1]) + "/" + str(time.localtime()[2]), 35, 12, False, 2)
    display_font(font.digiface_11, str(time.localtime()[3]) + ":" + str(time.localtime()[4]) + ":" + str(time.localtime()[5]), 35, 0, False, 2)
    clock.settime()
    clock.drawClock()
    oled.show()
tim1 = Timer(1)
# 时钟的计时器
alarm = [21,3]
alarmFlag = 0
def timer2_tick(_):
    global alarm,alarmFlag
    if time.localtime()[3] == alarm[0] and time.localtime()[4] == alarm[1]:
        alarmFlag = 1
    if alarmFlag == 1:
        music.play('A#5:4')
tim2 = Timer(2)
tim2.init(period=1000, mode=Timer.PERIODIC, callback=timer2_tick)
def on_button_a_pressed(_):
    global alarmFlag,alarm
    if alarmFlag == 1:
        alarm = [-1,-1]
        alarmFlag = -1
button_a.event_pressed = on_button_a_pressed
# 闹钟

def showChar():
    # 显示所选字符
    global inputChoice,inputCharacter
    if inputChoice != "":
        oled.fill_rect(0, 48, 128, 16, 0)
        oled.DispChar(inputChoice + " " + inputCharacter[int(inputChoice,2)], 0, 48, 1)
        oled.show()
    else:
        oled.fill_rect(0, 48, 128, 16, 0)
        oled.show()
    

def on_touchpad_p_pressed(_):
    global inputChoice,inputCharacter
    if int(inputChoice + "0",2) < len(inputCharacter):
        inputChoice += "0"
        showChar()
    

touchpad_p.event_pressed = on_touchpad_p_pressed
# 点击P时

def on_touchpad_y_pressed(_):
    global inputChoice,inputCharacter
    if int(inputChoice + "1",2) < len(inputCharacter):
        inputChoice += "1"
        showChar()
touchpad_y.event_pressed = on_touchpad_y_pressed
# 点击Y时

def on_touchpad_t_pressed(_):
    global inputChoice
    inputChoice = inputChoice[:-1]
    showChar()
touchpad_t.event_pressed = on_touchpad_t_pressed
# 点击T时

clockFlag = 0
def on_touchpad_h_pressed(_):
    global inputChoice,inputCharacter,cmd,clockFlag
    if inputChoice == "":
        return 0
    # 如果Bit没有值则不执行
    if clockFlag == 1:
        tim1.deinit()# 清除时钟
    if inputCharacter[int(inputChoice,2)] == "Del":
        cmd = cmd[:-1]
    elif inputCharacter[int(inputChoice,2)] == "Get":
        runCommand = cmd.split(" ")
        if runCommand[0] == "sudo":
            eval(cmd[5:])
        elif runCommand[0] == "print":
            oled.fill_rect(0, 0, 128, 16, 0)
            oled.DispChar(runCommand[1], 0, 0, 1)
            oled.show()
        elif runCommand[0] == "alarm":
            global alarm
            alarm = [int(runCommand[1]),int(runCommand[2])]
            oled.fill_rect(0, 0, 128, 16, 0)
            oled.DispChar("已设置一个" + runCommand[1] + ":" + runCommand[2] + "的闹钟", 0, 0, 1)
            oled.show()
        elif runCommand[0] == "link":
            wifi.connectWiFi(runCommand[1], runCommand[2])
            if wifi.sta.isconnected():
                oled.fill_rect(0, 0, 128, 16, 0)
                oled.DispChar("联网成功", 0, 0, 1)
                oled.show()
                ntptime.settime(8, "time.windows.com")
                oled.fill_rect(0, 0, 128, 32, 0)
                oled.DispChar("联网成功且可以访问互联网", 0, 0, 1, True)
                oled.show()
        else:
            oled.fill_rect(0, 0, 128, 16, 0)
            oled.DispChar("未知的指令:'" + runCommand[0] +"'", 0, 0, 1, True)
            oled.show()
        cmd = ""
    elif inputCharacter[int(inputChoice,2)] == "Clock":
        clockFlag = 1
        tim1.init(period=1000, mode=Timer.PERIODIC, callback=timer1_tick)
    else:
        cmd += inputCharacter[int(inputChoice,2)]
    oled.fill_rect(0, 32, 128, 16, 0)
    oled.DispChar(cmd, 0, 32, 1)
    # 转到命令
    oled.show()
    inputChoice = ""
    showChar()
    # 清空bit选择
touchpad_h.event_pressed = on_touchpad_h_pressed
# 点击H时