import pyautogui as bot
import time
import webbrowser

(screenWidth, screenHeight) = bot.size()

x = int(screenWidth / 3)
y = int(screenHeight / 2)
tries = 0

webbrowser.open_new('https://humanbenchmark.com/tests/reactiontime')

time.sleep(5)
bot.moveTo(x, y)
time.sleep(1)

bot.leftClick()

color = bot.pixel(x, y)
hexColor = '%02x%02x%02x' % color

while tries < 5:
    while hexColor != '4bdb6a':
        color = bot.pixel(x, y)
        hexColor = '%02x%02x%02x' % color
    
    bot.click()
    tries += 1
    hexColor = ''
    time.sleep(1)
    bot.click()