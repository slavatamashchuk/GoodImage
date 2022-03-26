add_library("sound")

Red=0
Blue=0
Green=0
Radius=5

WhatColor=None

Width=950
Height=950

quare=False

paint=False

logoend=False

onestartsound=True

loadingprogress=0

saveformat=None

def setup():
    global Width
    global Height
    print "                               "
    print "    ########             #     "
    print "  ##        #            #     "
    print " #                       #     "
    print " #      ######           #     "
    print "  ###     ####           #     "
    print "    #######   OOD        # MAGE"
    print "                               "
    print "Good program for good image    "
    print "                               "
    size (Width, Height)
    background (255)

def draw():
    global logoend
    global onestartsound
    global paint
    global Red
    global Blue
    global Green
    global Radius
    global Width
    global Height
    global loadingprogress
    
    slavchikSTIlogo=loadImage("rslavchikSTIlogo.png")
    GIlogo=loadImage("rGIlogo.png")
    startsound=SoundFile(this,"logo.mp3")
    
    if frameCount>=35:
        if onestartsound==True:
            onestartsound=False
            startsound.play()
    
#    if onestartsound==True:
#        onestartsound=False
#        startsound.play()
    if frameCount<14:
        image(slavchikSTIlogo, 0, 0)
    else:
        if frameCount<44:
            image(GIlogo, 0, 0)
        else:
            if logoend==False:
                fill (0)
                background(255)
                logoend=True
            else:
                if paint==True:
                    circle (mouseX, mouseY, Radius)
                    fill (Red, Blue, Green)
                    stroke (Red, Blue, Green)
                if Radius<=0:
                    Radius=1
                if Radius>9999:
                    Radius=9999
    
    if logoend==False:
        loadingprogress=loadingprogress+(width-100-50)/44
        if frameCount<=13:
            fill(0)
            stroke(255)
            rect(50, width-100, height-100, 50)
            fill (255)
            stroke (0)
            rect(60, width-95, loadingprogress+60, 40)
            fill(0)
            stroke(0)
        else:
            if frameCount<44:
                fill(255)
                stroke(0)
                rect(50, width-100, height-100, 50)
                fill (0)
                stroke (255)
                rect(60, width-95, loadingprogress+60, 40)
                fill(0)
                stroke(0)
    if quare==True:
        square(mouseX-Radius/2, mouseY-Radius/2, Radius)
    
def keyPressed():
    global Radius
    global Red
    global Blue
    global Green
    global quare
    global WhatColor
    global saveformat
    
    if keyCode==80: #p
        saveformat="png"
        
    if keyCode==74: #j
        saveformat="jpg"
    
    if keyCode==38:
        Radius+=2
        print "your radius"
        print Radius
        print "(pixels)"
        print ""
    if keyCode==40:
        Radius-=2
        print "your radius"
        print Radius
        print "(pixels)"
        print ""
        
    if keyCode==49: #1
        Red=0
        Blue=0
        Green=0
    if keyCode==50: #2
        Red=255
        Blue=0
        Green=0
    if keyCode==51: #3
        Red=255
        Blue=255
        Green=0
    if keyCode==52: #4
        Red=0
        Blue=255
        Green=0
    if keyCode==53: #5
        Red=0
        Blue=255
        Green=255
    if keyCode==54: #6
        Red=0
        Blue=190
        Green=255
    if keyCode==55: #7
        Red=0
        Blue=0
        Green=255
    if keyCode==56: #8
        Red=128
        Blue=0
        Green=128
    if keyCode==57: #9
        Red=255
        Blue=0 
        Green=128

    if keyCode==48: #0
        Red=255
        Blue=255
        Green=255
    
    if keyCode==81: #q
        quare=True
    else:
        quare=False
        
    if keyCode==82: #r
        WhatColor="Red"
        print "Your costum color is Red"
    if keyCode==71:
        WhatColor="Green" #g
        print "Your costum color is Green"
    if keyCode==66:
        WhatColor="Blue" #b
        print "Your costum color is Blue"

        
    if keyCode==37: 
        if WhatColor=="Red":
            Red-=1
        if WhatColor=="Green":
            Green-=1
        if WhatColor=="Blue":
            Blue-=1
    if keyCode==39:
        if WhatColor=="Red":
            Red+=1
        if WhatColor=="Green":
            Blue+=1
        if WhatColor=="Blue":
            Green+=1
            
    
    if keyCode==83: #s
        if frameCount>=44:
            if saveformat!="png" and saveformat!="jpg":
                print "you don't chose the format of save, if you want a png format for save your image press on 'p', but if you want a jpg format for sove your image press on 'j'"
            else:
                if saveformat=="png":
                    saveFrame("YourGoodImages/###########################################################################################################################################################################################################################################################.png")
                    print "image was save"
                else:
                    saveFrame("YourGoodImages/###########################################################################################################################################################################################################################################################.jpg")
                    print "image was save"
        else:
            print "GoodImage was loading, you can't save loading, please wait"


def mousePressed():
    global paint
    
    if mouseButton==LEFT: 
        paint=True
    else:
        paint=False
