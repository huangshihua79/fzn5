from lib.boppreh.keyboard import keyboard
import time
import sys

isExitKeyPress = False

def on_exit():
    print("Ready to exit.")
    global isExitKeyPress
    isExitKeyPress = True

def do_sleep(t):    
    global isExitKeyPress
    while t>0:
        if isExitKeyPress == True:            
            break
        if t < 1:
            time.sleep(t)
            break    
        time.sleep(1)
        t = t-1

numberOfRuns=0
def do_macro(actions):  
    global isExitKeyPress,numberOfRuns
    numberOfRuns = numberOfRuns + 1
    print("numberOfRuns:",numberOfRuns)
    for action in actions:
        if isExitKeyPress == True:           
            break

        #取得执行参数
        key = action["key"]
        delay = action["delay"]
        if "hold" in action:
            hold = action['hold']
        else:
            hold = False

        if "repeat" in action :
            repeat = action['repeat']
        else:
            repeat = 1
        
        #打印参数                
        actoinDesc = "["+key+"] ["+str(delay)+"]"
        if hold:
            actoinDesc += " [hold]"
        if repeat > 1:
            actoinDesc += " [repeat "+str(repeat)+"]"

        print("--",actoinDesc,)
        for i in range(repeat):
            if repeat > 1:
                print("   --",i+1)
            if key == "sleep" :
                do_sleep(delay)
            elif not hold:
                keyboard.press_and_release(key)
                do_sleep(delay)
            else:
                keyboard.press(key)
                do_sleep(delay)
                keyboard.release(key)
    


def FznStart(actions):
    global isExitKeyPress
    keyboard.add_hotkey("]",on_exit)
    keyboard.wait("[")
    while True:        
        do_macro(actions)
        if isExitKeyPress == True:
            break



