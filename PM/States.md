# 18-12-2023
First touches. Creation of repo and code base.
Successful detection of the metin closest to the position(0,0) on the screen, and interaction with it.

# 19-12-2023
for j in range(len(metin_names)):
            for i in range(6):
                img = screenshot(region=(MIN_X, MIN_Y, MAX_X, MAX_Y-MIN_Y))
                try:
                    index = j
                    posX,posY,_,_ = locate(metin_names[j], img, confidence=0.95)
                    check = True
                    break
                except ImageNotFoundException:
                    check = False
                    rotateCamera()
                    print("Oh no! No metin was found that matched the name...\nTime to rotate and find more :)")
                    continue
        if not check: continue


Use enumerate to loop over