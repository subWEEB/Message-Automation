#made with love by subweeb
import pyautogui as pt
import time
limit = input("Enter Limit: ")
message = input("Message: ")
i = 0
time.sleep(1)
while i<int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i+=1