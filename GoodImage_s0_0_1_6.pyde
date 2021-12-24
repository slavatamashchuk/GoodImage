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

def setup():
    global Width
    global Height
    print "                                   "
    print "    ########             #         "
    print "  ##        #            #         "
    print " #                       #         "
    print " #      ######           #         "
    print "  ###     ####           #         "
    print "    #######   OOD        # MAGE    "
    print "                                   "
    print "Good program for good image        "
    print "                                   "
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
#                if onestartsound==True:
#                    onestartsound=False
                logoend=True
#                startsound.play()
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
    
    if keyCode==86: #v
        print "                version menu"
        print ""
        print "                  s0.0.1.1"
        print ""
        print ""
        print "         Added coustumise of color"
        print ""
        print "                  s0.0.1.2"
        print ""
        print ""
        print "            Added save funktion"
        print ""
        print "                  s0.0.1.3"
        print ""
        print ""
        print "         fixed error in help menu"
        print "      the optimised size of the program" 
        print ""
        print "                  s0.0.1.4"
        print ""
        print ""
        print "     changed max radius of drawings circle"
        print ""
        print "                  s0.0.1.5"
        print ""
        print ""
        print "         deleted old square funktion"
        print "          added new square funktion"
        print "      the optimised size of the program"
        print ""
        print "                  s0.0.1.6" 
        print ""
        print ""
        print "           fixed error in help menu"
        print ""
        
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

    
    if keyCode==72: #h
        print "                         help menu"
        print ""
        print "for this munu press 'h'"
        print "for painting press 'left mouse button'"
        print "for not painting press 'mouse button'"
        print "for coler select press '1-9'"
        print "for erasederased press '0'"
        print "for big full stup or smol full stap press 'arrow top', 'arrow outside'"
        print "for 'version menu' press 'v'"
        print "for square mode press 'q', for don't quare mode prees 'random key'"
        print ""
    
    
    if keyCode==81: #q
        quare=True
    else:
        quare=False
    if keyCode==69: #e
        elips=True
    else:
        elips=False
        
    if keyCode==82:
        WhatColor="Red"
        print "Your costum color is Red"
    if keyCode==71:
        WhatColor="Green"
        print "Your costum color is Green"
    if keyCode==66:
        WhatColor="Blue"
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
            Green+=1
        if WhatColor=="Blue":
            Blue+=1
            
    
    if keyCode==83:
        saveFrame("####################################################################################################.png")
        print "image was save"
    


def mousePressed():
    global paint
    
    if mouseButton==LEFT: 
        paint=True
    else:
        paint=False
