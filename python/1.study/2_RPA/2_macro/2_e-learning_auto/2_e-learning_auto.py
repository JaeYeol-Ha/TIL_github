#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-

import sys
import pyautogui
import logging

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)
# window = pyautogui.getWindowsWithTitle("학습창 - Chrome")[0]
# window = pyautogui.getWindowsWithTitle("학습창 - Whale")[0]
# window.maximize()
# window.activate()
while True:
    btn_list = []
    btn_list.append(pyautogui.locateOnScreen("./btn_next2.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam0.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam0_1.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_confirm.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam2.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam3.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam4.png", confidence=0.8))
    btn_list.append(pyautogui.locateOnScreen("./btn_exam5.png", confidence=0.8))
    for btn in btn_list:
        if btn :  
            pyautogui.click(btn, duration=0.1)
            pyautogui.sleep(0.1)
    # window.minimize()
    logger.debug("대기 중")


