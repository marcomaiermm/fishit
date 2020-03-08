import cv2, time
import numpy as np
import pyautogui
import psutil
import random

from PIL import Image, ImageGrab
from .fish_area import CatchArea
from win32.win32gui import GetWindowText, GetForegroundWindow
from win32 import win32gui, win32process
from PyQt5.QtWidgets import *

class Fishit(QWidget):
    def __init__(self,w):
        super().__init__()
        self.widget = w
        self.fish=w.fish
    def CheckArea(self):
        self.status="idle..."
        self.fish_count=0

        is_block = False
        last_x = 0
        last_y = 0
        status=['fishing...','catch!','looting']
        while self.fish:
            try:
                dM01, dM10, dArea, fish_area = CatchArea()
                if self.active_window_process_name()=="WowClassic.exe":
                    if is_block == False:
                        last_x = 0
                        last_y = 0
                        pyautogui.press('1')
                        self.status=status[0]
                        self.widget.gui.status_edit.setText(str(self.status))
                        print("fishing...")
                        is_block = True
                    else:
                        b_x = 0
                        b_y = 0
                        if dArea > 0:
                            b_x = int(dM10 / dArea)
                            b_y = int(dM01 / dArea)
                        if last_x > 0 and last_y > 0:
                            if last_x != b_x and last_y != b_y:
                                is_block = False
                                if b_x < 1: b_x = last_x
                                if b_y < 1: b_y = last_y
                                print("Catch!")
                                self.status=status[1]
                                self.widget.gui.status_edit.setText(str(self.status))
                                pyautogui.moveTo(b_x, b_y+fish_area[1],0.2, pyautogui.easeOutQuad)
                                self.status=status[2]
                                self.widget.gui.status_edit.setText(str(self.status))
                                pyautogui.mouseDown(button='right')
                                pyautogui.mouseUp(button='right')
                                self.fish_count+=1
                                self.widget.gui.catched_edit.setText(str(self.fish_count))
                                wait_time=random.uniform(1,3)
                                print(wait_time)
                                self.widget.gui.status_edit.setText("waiting: " + str(round(wait_time,1)))
                                time.sleep(wait_time)
                        last_x = b_x
                        last_y = b_y     
            except:
                pass

    def returnState(self):
        return self.status
    def returnCatches(self):
        return self.fish_count

    def active_window_process_name(self):
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
        #pid[-1] is the most likely to survive last longer
        return psutil.Process(pid[-1]).name()  