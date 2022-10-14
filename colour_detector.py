from PIL import ImageGrab
import pyautogui as gui
import time # used to see performance of program

# gui.moveTo(250,200)

# end_time = time.time() + 1
# while end_time > time.time():

while True:
                        # bbox format = x_start, y_start, x_end, y_end
    image = ImageGrab.grab(bbox=(250,200,260,210))
    for y in range(0,10):
        for x in range(0,10):
            colour = image.getpixel((x,y))
            if colour == (255, 255, 84, 255):
                print("ligma")
            else:
                print("gay")

    # print("balls") # used to see how many times it checks ALL pixels/second