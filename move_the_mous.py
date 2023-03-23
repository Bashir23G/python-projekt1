import time

import pyautogui

# Move the mouse to (100, 100) on the screen
#pyautogui.moveTo(700, 400)

# Move the mouse to (100, 100) on the screen over 2 seconds
#pyautogui.moveTo(100, 100, duration=2)

# Double-click the left mouse button at (100, 100) on the screen
#pyautogui.click(700, 200, button='left', clicks=10)
# Drag the mouse to (200, 200) while holding down the left button
time.sleep(5)
#pyautogui.dragTo(300, 300, duration=100, button='left')
# Release the left button
#pyautogui.mouseUp()
#---------------------------------



# Press and release the 'Ctrl' and 'c' keys simultaneously
#pyautogui.hotkey('ctrl', 'c')

# Press and hold down the 'Shift' key
#pyautogui.keyDown('shift')

# Type the letter 'A'
#pyautogui.press('a')

# Release the 'Shift' key
#pyautogui.keyUp('shift')
# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Save the screenshot to a file
#screenshot.save('screenshot.png')
#--------------


#pip install pillow "it is used to image options

from PIL import Image

# Open an image file
img = Image.open("screenshot.png")

# Display the image
img.show()