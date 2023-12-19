from pyautogui import screenshot, locate, moveTo, click
from PIL import Image


class Metin:

    def __init__(self, distance):
        distance = self.distance

    def getDistance(self):
        """Return the distance to the metin

        Returns:
            int: Distance, in pixels, from the middle of the screen to the Metin
        """
        return self.distance

    def setDistance(self, pix):
        """Set the distance, from the middle of the screen to the Metin, to pix

        Args:
            pix (int): distance to be set to.
        """
        self.distance = pix

class MetinDetector:
    """_summary_
    """
    def __init__(self):
        pass


    def detectorSetup(self):
        """_summary_
        """
        pass


# Search window scale
MIN_X = 0
MIN_Y = 31
MAX_X = 1024
MAX_Y = 800
# Paths
METIN_NAME_IMG_PATH = 'img/metin_name.png'

if __name__  ==  "__main__":
    name_img = Image.open(METIN_NAME_IMG_PATH)
    img = screenshot(region=(MIN_X,MIN_Y,MAX_X,MAX_Y))
    img.save('img/print.png')
    
    

    x,y,w,h = locate(name_img, img, confidence=0.95)

    print("pos X: "+ str(x) + "\npos Y: "+str(y)+"\nwidth: "+str(w)+"\nheight: "+str(h))
    
    moveTo(x+30,y+80)
    click()

    # Initialize the detector
    # con = MetinDetector()
    # con.detectorSetup()