import pyautogui

pyautogui.sleep(1)

window = pyautogui.getWindowsWithTitle("NoxPlayer")[0]
window.activate()
# window.maximize()
# print(window.size)
# Size(width=1014, height=581) 기준

# # 데이터 초기화
# icon_nier = pyautogui.locateOnScreen("icon_nier.png", confidence=0.7)
# pyautogui.mouseDown(icon_nier, duration=0.5)
# pyautogui.sleep(1)
# pyautogui.mouseUp()
# icon_nier = pyautogui.locateOnScreen("nier_app_info.png", confidence=0.7)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(1)
# icon_nier = pyautogui.locateOnScreen("nier_app_info2.png", confidence=0.7)
# pyautogui.moveTo(icon_nier, duration=0.5)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(1)
# while True:
#     icon_nier = pyautogui.locateOnScreen("nier_app_info3.png", confidence=0.7)
#     pyautogui.moveTo(icon_nier, duration=0.5)
#     pyautogui.click(icon_nier, duration=0.5)
#     pyautogui.sleep(1)
#     icon_nier = pyautogui.locateOnScreen("nier_app_info4.png", confidence=0.7)
#     if icon_nier : 
#         pyautogui.moveTo(icon_nier, duration=0.5)
#         pyautogui.click(icon_nier, duration=0.5)
#         pyautogui.sleep(3)
#         break
# icon_nier = pyautogui.locateOnScreen("home.png", confidence=0.7)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(1)

# # 게임 시작

# icon_nier = pyautogui.locateOnScreen("icon_nier.png", confidence=0.7)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(45)

# while True:
#     icon_nier = pyautogui.locateOnScreen("nier_start.png", confidence=0.7)
#     if icon_nier :
#         pyautogui.click(icon_nier, duration=0.5)
#         break
#     pyautogui.sleep(15)

# pyautogui.sleep(5)

# pyautogui.press("T")

# icon_nier = pyautogui.locateOnScreen("nier_agree.png", confidence=0.7)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(1)

# icon_nier = pyautogui.locateOnScreen("nier_yes.png", confidence=0.7)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(1)

# icon_nier = pyautogui.locateOnScreen("nier_yes.png", confidence=0.7)
# pyautogui.click(icon_nier, duration=0.5)
# pyautogui.sleep(1)
# while True :
#     icon_nier = pyautogui.locateOnScreen("nier_yes.png", confidence=0.7)
#     if icon_nier:
#         pyautogui.click(icon_nier, duration=0.5)
#         break
#     pyautogui.sleep(1)


# while True :
#     icon_nier = pyautogui.locateOnScreen("nier_name.png", confidence=0.7)
#     if icon_nier:
#         pyautogui.click(icon_nier, duration=0.5)
#         pyautogui.sleep(0.5)
#         pyautogui.write("2B")
#         icon_nier = pyautogui.locateOnScreen("nier_name.png", confidence=0.7)
#         pyautogui.click(icon_nier, duration=0.5)
#         pyautogui.sleep(1)
#         pyautogui.press("T")
#         pyautogui.sleep(1)
#         pyautogui.press("G")
#         pyautogui.sleep(1)
#         pyautogui.press("T")
#         break
#     pyautogui.sleep(1)    

# # SKIP 지점(캡처필요)
# pyautogui.sleep(60)
# pyautogui.press("C")
# pyautogui.sleep(1)  
# pyautogui.press("Z")
# pyautogui.sleep(1)    
# pyautogui.press("T")
# pyautogui.sleep(30)  

# #Auto
# pyautogui.press("E")
# pyautogui.sleep(1)  
# pyautogui.press("C")
# pyautogui.sleep(60)  
# pyautogui.press("Q")
# pyautogui.sleep(10)  

# while True :
#     pyautogui.press("E")    
#     icon_nier = pyautogui.locateOnScreen("nier_auto.png", confidence=0.7)
#     if icon_nier:
#         pyautogui.sleep(5)  
#         pyautogui.press("C")
#         break
#     pyautogui.sleep(1)  
# pyautogui.sleep(10)  

# while True :
#     pyautogui.press("E")    
#     icon_nier = pyautogui.locateOnScreen("nier_auto.png", confidence=0.7)
#     if icon_nier:
#         pyautogui.sleep(5)  
#         pyautogui.press("C")
#         break
#     pyautogui.sleep(1)  

# pyautogui.sleep(20)  
# pyautogui.press("E")
# pyautogui.sleep(1)  
# pyautogui.press("Z")
# pyautogui.sleep(2)  
# pyautogui.press("T")
# pyautogui.sleep(8)  
# pyautogui.press("X")

# # 선물함 열기
# pyautogui.sleep(120)  
# pyautogui.press("Z")
# pyautogui.sleep(1)  
# pyautogui.press("Z")
# pyautogui.sleep(3)  
# pyautogui.press("B")
# pyautogui.sleep(2)  
# pyautogui.press("esc")
# pyautogui.sleep(2)  
# pyautogui.press("esc")
# pyautogui.sleep(2)  
# pyautogui.press("esc")

# pyautogui.sleep(1)  
# pyautogui.press("Y")
# pyautogui.sleep(1)  
# pyautogui.press("Y")
# pyautogui.sleep(1)  

# for _ in range(20):
#     pyautogui.press("E")
#     pyautogui.sleep(1)  
# for _ in range(15):
#     pyautogui.press("V")
#     pyautogui.sleep(1)  


# while True :    
#     pyautogui.press("V")
#     pyautogui.sleep(1) 
#     icon_nier = pyautogui.locateOnScreen("nier_collabo.png", confidence=0.7)
#     if icon_nier:
#         pyautogui.click(icon_nier, duration=0.5)
#         icon_nier = pyautogui.locateOnScreen("nier_collabo2.png", confidence=0.7)
#         if icon_nier:    
#             break       

# pyautogui.sleep(3)  
# pyautogui.press("B")
# pyautogui.sleep(1)  
# pyautogui.press("T")
# pyautogui.sleep(12)  
# pyautogui.press("Z")

while True :    
    pyautogui.press("Z")
    pyautogui.sleep(1) 
    icon_nier = pyautogui.locateOnScreen("nier_re.png", confidence=0.7)
    if icon_nier:
        pyautogui.press("R")
        break

pyautogui.sleep(15)  
pyautogui.press("Q")
pyautogui.sleep(3)  
pyautogui.press("T")
pyautogui.sleep(12)  
pyautogui.press("Z")
pyautogui.sleep(5)  

# 단차 6번 뽑기
T = 6
while T > 0 :        
    pyautogui.sleep(1)
    pyautogui.press("Z")    
    pyautogui.sleep(3) 
    icon_nier = pyautogui.locateOnScreen("nier_re.png", confidence=0.7)
    if icon_nier:
        pyautogui.press("Y")
        pyautogui.sleep(1) 
        pyautogui.press("T")
        T -= 1

pyautogui.sleep(5)  
icon_nier = pyautogui.locateOnScreen("home.png", confidence=0.7)
pyautogui.click(icon_nier, duration=0.5)