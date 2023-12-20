from pyautogui import position, screenshot, locate, moveTo, click, dragTo, press, ImageNotFoundException,  FailSafeException
from PIL import Image
from time import sleep, time
import signal

class Metin:

    def __init__(self, distance:int):
        distance = self.distance

    def getDistance(self):
        """Return the distance to the metin

        Returns:
            int: Distance, in pixels, from the middle of the screen to the Metin
        """
        return self.distance

    def setDistance(self, pix:int):
        """Set the distance, from the middle of the screen to the Metin, to pix

        Args:
            pix (int): distance to be set to.
        """
        self.distance = pix

def handler(signum,  frame):
    print("Quitting...")
    proceed = False
    exit(1)

def rotateCamera():
    moveTo(DEAD_CENTER_X, DEAD_CENTER_Y)
    click()
    dragTo(DEAD_CENTER_X + 10, DEAD_CENTER_Y, 1, button='right')

def mouseClick(x:int, y:int, string:str='primary'):
    moveTo(x, y)
    click(button=string)

def metinScanner(metin_name):
    proceed:bool = True
    posX, posY = 0, 0
    while(proceed):
        print("Searching...")
        img = screenshot(region=(MIN_X, MIN_Y, MAX_X, MAX_Y-MIN_Y))
        try:
            posX,posY,_,_ = locate(metin_name, img, confidence=0.95)
        except ImageNotFoundException:
            print("Oh no! No metin was found that matched the name...\nTime to rotate and find more :)")
            rotateCamera()
            continue
        # position to move to
        mouseClick(posX+OFFSET_X, posY+OFFSET_Y)
        # hitbox temporary nulling 
        mouseClick(HITBOX_ELIM_X, HITBOX_ELIM_Y, 'right')
        # pull mobs to avoid problem on Metin travelling
        #mouseClick(HITBOX_ELIM_X-18, HITBOX_ELIM_Y, 'right')
        print("Target acquired...")

        sleep(18)

# Constant positions
HITBOX_ELIM_X = 614
HITBOX_ELIM_Y = 778
DEAD_CENTER_X = 510
DEAD_CENTER_Y = 448

# Search window scale
MIN_X = 0
MIN_Y = 31
MAX_X = 1024
MAX_Y = 800
OFFSET_X = 40
OFFSET_Y = 80
# Paths
METIN_NAME_IMG_PATH = 'img/metin_name.png'
SURPRISE_METIN_NAME_IMG_PATH = 'img/surprise_metin.png'
if __name__  ==  "__main__":
    name_img = Image.open(METIN_NAME_IMG_PATH)
    signal.signal(signal.SIGINT,  handler)
    metinScanner(name_img)
