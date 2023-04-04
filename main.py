import pyautogui
import time
import random


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def auto_mouse():
    time.sleep(3)

    pyautogui.PAUSE = 2.5
    pyautogui.FAILSAFE = True
    print(pyautogui.size().width)
    screenWidth = pyautogui.size().width
    screentHeight = pyautogui.size().width

    # pyautogui.hotkey('alt', 'tab', interval=0.1)
    # pyautogui.hotkey('alt', 'tab', interval=0.1)

    while True:

        randomWidth = random.randint(0, screenWidth)
        randomHeight = random.randint(0, screentHeight)
        random_num = random.random()
        width = randomWidth
        height = randomHeight
        # print(width, height)

        pyautogui.moveTo(width, height, duration=random_num)
        time.sleep(random_num)

        if 0.6 < random_num < 0.7:
            pyautogui.press('ctl')
        if 0.8 < random_num < 0.9:
            pyautogui.press('alt')

        pyautogui.moveTo(width, height, duration=random_num)
        time.sleep(random_num)

        # pyautogui.hotkey('alt', 'tab', interval=0.1)
        # with pyautogui.hold("alt"):
        #     pyautogui.press(["tab"])

        if 0.1 <= random_num < 0.3:
            pyautogui.keyDown('alt')
            time.sleep(.2)
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.keyUp('alt')
        if 0.3 <= random_num < 0.5:
            pyautogui.keyDown('alt')
            time.sleep(.2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.keyUp('alt')
        if 0.7 <= random_num < 0.9:
            pyautogui.keyDown('alt')
            time.sleep(.2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.keyUp('alt')

        pyautogui.moveTo(width, height, duration=random_num)
        time.sleep(random_num)

        if 0.3 < random_num < 0.5:
            pyautogui.press('shift')

        pyautogui.moveTo(width, height, duration=random_num)
        time.sleep(random_num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    auto_mouse()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
