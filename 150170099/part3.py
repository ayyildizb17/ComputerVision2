#BUSE AYYILDIZ 150170099

import cv2
import cv2 as cv
import numpy as np
import pyautogui
import time

time.sleep(1)

for i in range(1,300):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('test_{}.png'.format(i))
    img = cv2.imread('test_{}.png'.format(i))
    cropped_img = img[810:1920, 1055:1455] #obtain a cropped image for shape detection
    gray = cv2.cvtColor(cropped_img,cv2.COLOR_BGR2GRAY)
    ret, thrash = cv2.threshold(gray, 240, 255, cv2.CHAIN_APPROX_NONE)
    # finding contours from threshold img
    contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        # if triangle press a
        if len(approx) == 3:
            pyautogui.keyUp('D')
            pyautogui.keyUp('S')
            pyautogui.keyUp('F')
            pyautogui.keyDown('A')
        # if triangle press a
        if len(approx) == 4:
            pyautogui.keyUp('D')
            pyautogui.keyUp('A')
            pyautogui.keyUp('F')
            pyautogui.keyDown('S')
        # if star(10 corner) press f
        if len(approx) == 10:
            pyautogui.keyUp('A')
            pyautogui.keyUp('S')
            pyautogui.keyUp('F')
            pyautogui.keyDown('D')
        # if hexagonal press f
        if len(approx) == 6:
            pyautogui.keyUp('A')
            pyautogui.keyUp('S')
            pyautogui.keyUp('D')
            pyautogui.keyDown('F')
        # relasing buttons
        pyautogui.keyUp('D')
        pyautogui.keyUp('S')
        pyautogui.keyUp('F')
        pyautogui.keyUp('A')



