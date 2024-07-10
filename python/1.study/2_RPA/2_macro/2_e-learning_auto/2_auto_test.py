import os
import pyautogui

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMG_DIR = os.path.join(BASE_DIR,"static","img")

pyautogui.locateOnScreen(IMG_DIR + "/btn_next2.png", confidence=0.8)