
import pyautogui
import pyperclip
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# Step 1: Open Chrome
print("Opening Chrome...")

pyautogui.hotkey('win', 'r')
time.sleep(2)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)

# Step 2: Open website
print("Opening website...")

pyautogui.write(
    'https://www.motilaloswal.com/share-market'
)
pyautogui.press('enter')
time.sleep(10)

# Step 3: Copy website content
print("Copying website content...")

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

data = pyperclip.paste()

# Step 4: Open Excel
print("Opening Excel...")

pyautogui.hotkey('win', 'r')
time.sleep(2)
pyautogui.write('excel')
pyautogui.press('enter')
time.sleep(8)

# Step 5: Paste data into Excel
print("Pasting data into Excel...")

pyautogui.write('Date & Time')
pyautogui.press('tab')
pyautogui.write('Website Data')
pyautogui.press('enter')

pyautogui.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
pyautogui.press('tab')

pyperclip.copy(data)
pyautogui.hotkey('ctrl', 'v')

# Step 6: Save Excel
print("Saving Excel...")

time.sleep(3)
pyautogui.hotkey('ctrl', 'shift', 's')
time.sleep(3)

filename = 'daily_report_' + datetime.now().strftime('%Y-%m-%d') + '.xlsx'

pyautogui.write(filename)
pyautogui.press('enter')
time.sleep(4)
pyautogui.press('enter')
time.sleep(3)

# Step 7: Screenshot
print("Taking screenshot...")

pyautogui.screenshot().save(
    'daily_report_screenshot.png'
)

print("Task completed successfully!")
