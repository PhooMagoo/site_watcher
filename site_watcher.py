### Watch a site to see when a product becomes available for purchase.

# TODO: Add support for other sites.

import time                     # For waiting.
import winsound                 # For alerting me with annoying sounds.
import pyautogui                # For screen watching.
import bs4, webbrowser          # For website handling.
from selenium import webdriver  # More website stuff.
from pprint import pprint       # For nice text.

#######################################################

# Our annoying noise to notify us of a change.
def annoy(frequency, duration):
    winsound.Beep(frequency, duration)

#######################################################

# Get the page we're going to be watching like a hawk.
pprint(r'What page are we watching?')
page = input(r'> ')

# What site is this?
# TODO: Add more later, like GameStop and Amazon.
if 'bestbuy' in page:
    site = 'BestBuy'
else:
    site = 'Other'

########################################################

bb_color = (255, 224, 0) # The yellow color for Best Buy.

# Open a browser and navigate to the provided page.
browser = webdriver.Chrome()
browser.get(page)

while True:
    # Refresh the page.
    browser.refresh()

    img = pyautogui.screenshot(r'C:\Users\PhooM\Desktop\Code\Scripts\Python\site.png')

    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) == bb_color:
                pprint('Color found!')
                annoy(2500, 1000)
                break

    pprint('Refreshing.')
    time.sleep(60)
