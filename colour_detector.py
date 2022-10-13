from PIL import ImageGrab
import pyautogui as gui

#gui.moveTo(250,200)

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

    