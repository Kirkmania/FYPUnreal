from PIL import ImageGrab as ig
import time
import win32api
import numpy as np
import ctypes
import keyboard
import os
import autopy


# C struct redefinitions FROM https://stackoverflow.com/questions/50601200/pyhon-directinput-mouse-relative-moving-act-not-as-expected
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions
def MouseMoveTo(x, y):
    relative_x = x - 970 + 40 # + 50 for more central position
    relative_y = y - 540 + 40
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(relative_x, relative_y, 0, 0x0001, 0, ctypes.pointer(extra))
    print("relative movement: (", relative_x, ", ", relative_y,")")

    command = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))


# example code
def leftclick():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    time.sleep(0.5)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    time.sleep(0.2)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    #ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    #ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    #time.sleep(0.01)
    
#find pixels + shoot

def Compareaa():
    image = ig.grab().convert("RGBA")
    
    pix = np.array(image)
    # for i in range(510,570):
    #     for j in range(950,970):
    for i in range(0,1080,10):
        for j in range(0,1920,10):
            #pix = image.getpixel((j,i))
            if((int(pix[i][j][0])>=180)&(int(pix[i][j][0])<=255) & (int(pix[i][j][1])>=0) & (int(pix[i][j][1])<=20) & (int(pix[i][j][2])>=0) & (int(pix[i][j][2])<=40)): # & (int(pix[i][j][1])>=63) & (int(pix[i][j][1])<=93) & (int(pix[i][j][2])>=250) & (int(pix[i][j][2])<=255)
                print("Found red at: (", j, ", ", i, ")")
                MouseMoveTo(j,i) #- if any way of simulating mouse movement would render camera movement, this would be aimbot too
                leftclick()
                break
                        
                    
            
        else:
            continue
        break
            
#img = ig.grab().convert("RGBA")
#ar = np.array(img)
#print(ar.shape)
#print(ar[1][1])
print("Triggerbot started- change window to valorant, z to stop")
while(True):
    
    try:
        #if keyboard.is_pressed('v'):
        Compareaa()
            #compaa2()
            
        if keyboard.is_pressed('z'):
            print("stopped")
            break
            
            
    except:
        pass
        
#compaa2()
os.system("PAUSE")    