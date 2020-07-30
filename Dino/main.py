import pyautogui
from PIL import Image, ImageGrab
import numpy as np
import time

def hit(key):
    pyautogui.keyDown(key)

def colide(data):
    for i in range(1120,1180):
        for j in range (400,420):
            if data[i,j]<100:
                return True
    return False

if __name__ == "__main__":
    time.sleep(3)
    hit('up')
    x=1;
    while True:
        image=ImageGrab.grab().convert('L')
        data = image.load()
        if colide(data)==True:
            print('Cactus',x)
            hit('up')
            x=x+1
