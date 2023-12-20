# Presentation
This document will take the ideas and thought process through each step 

# First steps
- Develop repo structure
- Learn how to capture certain areas of the screen
    - Future idea: Get game window by 2 clicks (top-left and bot-right)
- Search the image for *Metin Name*.
- Calculate the distance from all the positions to the middle of the game screen.
- Pass a M1 output.
- Special case: No metins on screen.
    - First  attempt: turn the camera by 20º every screening process until there's a metin found


# Code
## Classes

### Metin
Class to represent the info about a Metin found:
    - distance (from middle of screen to its location)
In development.
Will be used for closest Metin found and potentially Metin queueing.

### MetinDetector
Class to harbor all calculations done between the player and Metins
**Dropped** -> no longer used, unrequested additional complexity
## Imaging
Starts at (0, 30) down to (1024, 800)
(0, 30) --- (1024, 30)
|                   |
|                   |
(0,800) --- (1024,800)

Time per Metin of Murder -> 16 secs
