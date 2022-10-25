from PIL import ImageGrab
import pyautogui as gui
import keyboard
import time # used to see performance of program

# gui.moveTo(250,200)

# end_time = time.time() + 1
# while end_time > time.time():

while True:
                        # bbox format = x_start, y_start, x_end, y_end
    image = ImageGrab.grab(bbox=(955,535,965,545))
    for y in range(0,10):
        for x in range(0,10):
            colour = image.getpixel((x,y))
            r, g, b = colour[0], colour[1], colour[2]
            if 215 < r > 255 and 215 < g > 255 and 0 < b > 80:
                if keyboard.is_pressed('w') == False and keyboard.is_pressed('s') == False:
                    if keyboard.is_pressed('a') == False and keyboard.is_pressed('d') == False:
                        gui.press(".")
                        break
                    if keyboard.is_pressed('a') == True and keyboard.is_pressed('d') == True:
                        gui.press(".")
                        break
            

    # print("balls") # used to see how many times it checks ALL pixels/second