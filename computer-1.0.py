from mpython import *
# 引用库

inputCharacter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '`', '-', '=', '{', '}', '|', ':', '"', '<', '>', '?', '[', ']', '\\', ';', "'", ',', '.', '/', ' ', 'Del', 'Get']
# 所有字符
inputChoice = ""
# 选择的字符
cmd = ""
# 命令

oled.fill(0)
oled.DispChar("miniComputer 1.0", 0, 0, 1)
oled.show()
# 重启刷新

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

def on_touchpad_h_pressed(_):
    global inputChoice,inputCharacter,cmd
    if inputChoice == "":
        return 0
    # 如果Bit没有值则不执行
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
        cmd = ""
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