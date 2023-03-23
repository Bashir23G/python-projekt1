import pyautogui
import time

word ="Ramadan Mubark Abo Aliser"   # replace "Hello" with the word you want to repeat
count = 0

time.sleep(5)  # wait for 5 seconds before starting

while count < 10:
    pyautogui.typewrite(word)  # type the word
    pyautogui.press("enter")  # press "Enter" key
    count += 1        # increment count
