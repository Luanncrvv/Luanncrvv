from pyautogui import *
import pyautogui
from time import sleep
import mouse
import pygetwindow


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def check_data():
    data = pyautogui.locateOnScreen(
        'aLuan\\ImagesTeams\\DataEHora.png', confidence=0.5)

    if data != None:
        click(x=1147, y=1060)
        sleep(1)
        click(x=795, y=1013)
        sleep(1)
        click(x=726, y=975)
        sleep(1)
        click(x=89, y=176)
        sleep(1)
        click(x=262, y=192)
        sleep(1)
        click(x=794, y=507)
        sleep(5)
        click(x=1612, y=1014)
        sleep(2)  # confirmar

        return True
    return False


def main():
    while True:
        if check_data():
            sleep(900)


main()
