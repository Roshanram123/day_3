import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

print("open the chrome browser")
time.sleep(3)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('chrome\n', interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
print("step 2: open the google.com")
pyautogui.write('https://www.accuweather.com/en/in/kancheepuram/190796/weather-forecast/190796')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.hotkey('ctrl','c')
time.sleep(1)
pyautogui.hotkey('win','r')
time.sleep(1)
pyautogui.typewrite('notepad\n', interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl','v')
