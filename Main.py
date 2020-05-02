from ScreenManager import *
from LandManager import *
import keyboard  # using module keyboard
import os
import time
import sys
import subprocess
class MainGame():
    def __init__(self):
        self.topp = 0
        self.leftp = 0
        self.GameSetting = ""
        self.Game(self.SelectGameSetting())
    def SelectGameSetting(self):
        inp = input("Select Game Setting. \n\"A\" for Archipelago.\n\"MA\" for Mountainy Archipelago. \n\"MI\" for Mountainy Islands. Anything else for random.")
        if inp == "A":
            return SettingLand("A")
        elif inp == "MA":
            return SettingLand("MA")
        elif inp == "MI":
            return SettingLand("MI")
        else:
            return SettingLand("R")
    def Game(self, mapval=SettingLand("R")):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('w'):
                    
                    self.topp -= 1
                    Screen(mapval, topp=self.topp, leftp=self.leftp)
                    time.sleep(0.25)
                if keyboard.is_pressed('a'):
                    
                    self.leftp -= 1
                    Screen(mapval, topp=self.topp, leftp=self.leftp)
                    time.sleep(0.25)
                if keyboard.is_pressed('s'):
                    
                    self.topp += 1
                    Screen(mapval, topp=self.topp, leftp=self.leftp)
                    time.sleep(0.25)
                if keyboard.is_pressed('d'):
                    
                    self.leftp += 1
                    Screen(mapval, topp=self.topp, leftp=self.leftp)
                    time.sleep(0.25)
                if keyboard.is_pressed('n'):
                    print(('\n')*35)
                    Screen(mapval, topp=self.topp, leftp=self.leftp)
                    time.sleep(0.25)
            except Exception as e:
                print(e)

MainGame()
