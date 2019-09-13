#Paint.py
from pygame import * #all graphics programs will need this
from random import *
from math import *
from tkinter import *

root=Tk()
root.withdraw()
font.init()

szFont=font.SysFont("Arial Unicode MS",17) #creating a font object from system fonts

init()
      #r   g b
RED  =(255,0,0) #tuple - a list that can not be changed!
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

PEACH=(255,210,127) #colour of tool ellipses
DPEACH=(255,184,104) #dark peach- colour of tool ellipses when selected
YELLOW=(255,255,0)


size=(1280,960) #screen resolution
screen=display.set_mode(size)#creating a 1280x960 window

tool="None"  #current tool
toolInfo=" "   #blank strings for tool information
toolInfo1=" "
toolInfo2=" "
toolInfo3=" "
toolInfo4=" "
toolInfo5=" "
toolInfo6=" "

col=BLACK  #default colour

running=True #boolean variable
sz=5  #default size

newSpots=[]
myClock=time.Clock()



#tool rectangles
pencilRect=Rect(20,30,60,60)
eraserRect=Rect(100,30,60,60)
paintbrushRect=Rect(20,110,60,60)
dropperRect=Rect(100,110,60,60)
recttoolRect=Rect(20,190,60,60)
ellipseRect=Rect(100,190,60,60)
lineRect=Rect(20,270,60,60)
sprayRect=Rect(100,270,60,60)
fillRect=Rect(20,350,60,60)
highlightRect=Rect(100,350,60,60)
undoRect=Rect(20,430,60,60)
redoRect=Rect(100,430,60,60)
openRect=Rect(20,510,60,60)
saveRect=Rect(100,510,60,60)

#sticker rectangles
izayaRect=Rect(10,750,138,190)
shizuoRect=Rect(151,750,138,190)
kidaRect=Rect(292,750,138,190)
mikadoRect=Rect(433,750,138,190)
anriRect=Rect(725,750,138,190)
kadotaRect=Rect(856,750,138,190)
celtyRect=Rect(997,750,138,190)
shinraRect=Rect(1132,750,138,190)


paletteRect=Rect(579,774,142,142)
canvasRect=Rect(180,30,920,700)


#tool information rectanlges
szBar=Rect(20,590,50,20)
coordBar=Rect(82,590,75,20)
infoBar=Rect(20,620,135,110)



highlightHead=Surface((20,20),SRCALPHA) #creating a surface for highlight tool
draw.circle(highlightHead,(255,255,0,70),(10,10),10) 


#########################################################
#loading images
background=image.load("images/background.png")
paletteIcon=image.load("images/colourpalette.png")
pencilIcon=image.load("images/penciltoolicon.png")
eraserIcon=image.load("images/eraser.png")
paintbrushIcon=image.load("images/paintbrush.png")
dropperIcon=image.load("images/dropper.png")
recttoolIcon=image.load("images/recttool.png")
ellipseIcon=image.load("images/ellipse.png")
lineIcon=image.load("images/linetool.png")
spraypaintIcon=image.load("images/spraypaint.png")
fillIcon=image.load("images/fill.png")
highlightIcon=image.load("images/highlight.png")
undoIcon=image.load("images/undo.png")
redoIcon=image.load("images/redo.png")
openIcon=image.load("images/open.png")
saveIcon=image.load("images/save.png")


#loading stickers
izayaIcon=image.load("images/izaya.png")
shizuoIcon=image.load("images/shizuo.png")
kidaIcon=image.load("images/kida.png")
mikadoIcon=image.load("images/mikado.png")
shinraIcon=image.load("images/shinra.png")
celtyIcon=image.load("images/celty.png")
kadotaIcon=image.load("images/kadota.png")
anriIcon=image.load("images/anri.png")


#loading images of stickers with an outline
izayaSelect=image.load("images/izayaS.png")
shizuoSelect=image.load("images/shizuoS.png")
kidaSelect=image.load("images/kidaS.png")
mikadoSelect=image.load("images/mikadoS.png")
anriSelect=image.load("images/anriS.png")
kadotaSelect=image.load("images/kadotaS.png")
celtySelect=image.load("images/celtyS.png")
shinraSelect=image.load("images/shinraS.png")

peachBg = image.load("images/peachBg.png");

screen.blit(background,(0,0))
###############################################################
draw.rect(screen,WHITE,canvasRect) #drawing the canvas only once
###############################################################


draw.ellipse(screen,BLACK,paletteRect)

undoL=[(screen.subsurface(canvasRect)).copy()] #captures blank screen for first element of undo list
redoL=[] #empty redo list

##############################################################
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if canvasRect.collidepoint(mx,my):
                redoL=[]  #resets redo list 
            if evt.button==1:#left click
                if undoRect.collidepoint(mx,my):
                    tool="Undo"
                    if len(undoL)>1:  #if there's atleast 2 elements in the undo list 
                        screen.blit(undoL[-2],(180,30)) #blits the second last element
                        redoL.append(undoL.pop()) #adds last element to redo list

                if redoRect.collidepoint(mx,my):
                    tool="Redo"
                    if len(redoL)>0:  #if there's atleast 1 element in the redo list
                        screen.blit(redoL[-1],(180,30)) #blits the last element of what was added from undo list
                        undoL.append(redoL.pop()) #adds last element back to undo list
                back=screen.copy()
                sx,sy=evt.pos #tuple (x,y) position where you click
            #changing the size
            elif evt.button==5:#scroll down
                if sz>1:
                    sz-=1
                    
            elif evt.button==4:#scroll up
                if sz<50:
                    sz+=1
        if evt.type==MOUSEBUTTONUP:               #prevents from capturing screen when scrolling to switch sizes
            if canvasRect.collidepoint(mx,my) and evt.button!=4 and evt.button!=5:
                undoL.append(screen.subsurface(canvasRect).copy())
                       
  
    mx,my=mouse.get_pos()  
    mb=mouse.get_pressed()


    

    #drawing tool ellipses    
    draw.ellipse(screen,PEACH,pencilRect)
    draw.ellipse(screen,PEACH,eraserRect)
    draw.ellipse(screen,PEACH,paintbrushRect)
    draw.ellipse(screen,PEACH,dropperRect)
    draw.ellipse(screen,PEACH,ellipseRect)
    draw.ellipse(screen,PEACH,recttoolRect)
    draw.ellipse(screen,PEACH,sprayRect)
    draw.ellipse(screen,PEACH,fillRect)
    draw.ellipse(screen,PEACH,highlightRect)
    draw.ellipse(screen,PEACH,lineRect)
    draw.ellipse(screen,PEACH,undoRect)
    draw.ellipse(screen,PEACH,redoRect)
    draw.ellipse(screen,PEACH,openRect)
    draw.ellipse(screen,PEACH,saveRect)

    #drawing tool information rectangles
    draw.rect(screen,DPEACH,szBar)
    draw.rect(screen,DPEACH,coordBar)
    draw.rect(screen,DPEACH,infoBar)


   
    coordx=str(mx) #converting integers to strings to display as text
    coordy=str(my)
    sz1=str(sz)   
    textSz="Size:"+sz1  
    textCoord="x:"+coordx+" y:"+coordy
    
    displaySz=szFont.render(textSz,True,BLACK)  #rendering the text
    displayCoord=szFont.render(textCoord,True,BLACK)
    

    screen.blit(displaySz,(20,590))  #displaying the size and coordinates
    screen.blit(displayCoord,(82,590))
    


    ########################################################
    #tool selection
 
    if tool=="Pencil":
        draw.ellipse(screen,DPEACH,pencilRect)
    if tool=="Eraser":
        draw.ellipse(screen,DPEACH,eraserRect)
    if tool=="Paintbrush":
        draw.ellipse(screen,DPEACH,paintbrushRect)
    if tool=="Dropper":
        draw.ellipse(screen,DPEACH,dropperRect)
    if tool=="Rectangle":
        draw.ellipse(screen,DPEACH,recttoolRect)
    if tool=="Ellipse":
        draw.ellipse(screen,DPEACH,ellipseRect)
    if tool=="Line":
        draw.ellipse(screen,DPEACH,lineRect)
    if tool=="Spraypaint":
        draw.ellipse(screen,DPEACH,sprayRect)
    if tool=="Highlight":
        draw.ellipse(screen,DPEACH,highlightRect)
    if tool=="Fill":
        draw.ellipse(screen,DPEACH,fillRect)
    if tool=="Undo":
        draw.ellipse(screen,DPEACH,undoRect)
    if tool=="Redo":
        draw.ellipse(screen,DPEACH,redoRect)
    if tool=="Open":
        draw.ellipse(screen,DPEACH,openRect)
    if tool=="Save":
        draw.ellipse(screen,DPEACH,saveRect)

    if tool=="Izaya" and mb[0] == 1:
        screen.blit(izayaSelect,(10,750))
    else:
        screen.blit(peachBg,(10,750))

    if tool=="Shizuo" and mb[0] == 1:
        screen.blit(shizuoSelect,(151,750))
    else:
        screen.blit(peachBg,(151,750))

    if tool=="Kida" and mb[0] == 1:
        screen.blit(kidaSelect,(292,750))
    else:
        screen.blit(peachBg,(292,750))

    if tool=="Mikado" and mb[0] == 1:
        screen.blit(mikadoSelect,(433,750))
    else:
        screen.blit(peachBg,(433,750))
    if tool=="Anri" and mb[0] == 1:
        screen.blit(anriSelect,(725,750))
    else:
        screen.blit(peachBg,(725,750))
        
    if tool=="Kadota" and mb[0] == 1:
        screen.blit(kadotaSelect,(856,750))
    else:
        screen.blit(peachBg,(856,750))
        
    if tool=="Celty" and mb[0] == 1:
        screen.blit(celtySelect,(997,750))
    else:
        screen.blit(peachBg,(997,750))
        
    if tool=="Shinra" and mb[0] == 1:
        screen.blit(shinraSelect,(1132,750))
    else:
        screen.blit(peachBg,(1132,750))
        
    if pencilRect.collidepoint(mx,my): #hovering over the tool gives a description
        toolInfo1="Click and drag the"    
        toolInfo2="left mouse button on"
        toolInfo3="the canvas."
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
             tool="Pencil"  #if clicked, tool is selected
       
    if eraserRect.collidepoint(mx,my):
        toolInfo1="Click and drag the"
        toolInfo2="left mouse button on"
        toolInfo3="the canvas."
        toolInfo4="Scroll to change the"
        toolInfo5="size of the eraser "
        toolInfo6=" "
        if mb[0]==1:
            tool="Eraser"
    if paintbrushRect.collidepoint(mx,my):
        toolInfo1="Click and drag the"
        toolInfo2="left mouse button on"
        toolInfo3="the canvas."
        toolInfo3="Scroll to increase"
        toolInfo4="or decrease size"
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Paintbrush"
    if dropperRect.collidepoint(mx,my):
        toolInfo1="Click anywhere on"
        toolInfo2="the canvas to select"
        toolInfo3="a colour."
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Dropper"
    if recttoolRect.collidepoint(mx,my):
        toolInfo1="Click and drag the"
        toolInfo2="left mouse button to"
        toolInfo3="create a rectangle."
        toolInfo4="Scroll to size 1 to"
        toolInfo5="draw a filled rectangle."
        toolInfo6=" "
        if mb[0]==1:
            tool="Rectangle"
    if ellipseRect.collidepoint(mx,my):
        toolInfo1="Click and drag the"
        toolInfo2="left mouse button to"
        toolInfo3="create an ellipse."
        toolInfo4="Scroll to size 1 to"
        toolInfo5="draw a filled ellipse."
        toolInfo6=" "
        if mb[0]==1:
            tool="Ellipse"
    if lineRect.collidepoint(mx,my):
        toolInfo1="Click and drag the"
        toolInfo2="left mouse button to"
        toolInfo3="create a line."
        toolInfo4="Scroll to change"
        toolInfo5="the width of the line. "
        toolInfo6=" "
        if mb[0]==1:
            tool="Line"
    if sprayRect.collidepoint(mx,my):
        toolInfo1="Click and drag the left"
        toolInfo2="mouse button. Click"
        toolInfo3="and hold to create"
        toolInfo4="more pixels."
        toolInfo5="Scroll to change the"
        toolInfo6="radius. "
        if mb[0]==1:
            tool="Spraypaint"
    if highlightRect.collidepoint(mx,my):
        toolInfo1="Click and drag the"
        toolInfo2="left mouse button to"
        toolInfo3="create a yellow"
        toolInfo4="transparent surface"
        toolInfo5="that highlights"
        toolInfo6="anything."
        if mb[0]==1:
            tool="Highlight"
    if fillRect.collidepoint(mx,my):
        toolInfo1="Click anywhere on the "
        toolInfo2="canvas to fill an area"
        toolInfo3="with the selected"
        toolInfo4="colour. "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Fill"
    if undoRect.collidepoint(mx,my):
        toolInfo1="Click to undo"
        toolInfo2="the last action."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Undo"
    if redoRect.collidepoint(mx,my):
        toolInfo1="Click to redo"
        toolInfo2="the last action."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Redo"
    if openRect.collidepoint(mx,my):
        toolInfo1="Click to open the file"
        toolInfo2="explorer. Choose any"
        toolInfo3="file to open. Allowed"
        toolInfo4="file types: png,bmp,jpg,"
        toolInfo5="jpeg. "
        toolInfo6=" "
        if mb[0]==1:
            tool="Open"   
    if saveRect.collidepoint(mx,my):
        toolInfo1="Click to open the file"
        toolInfo2="explorer. Type in the"
        toolInfo3="desired file name and"
        toolInfo4="press save. Default"
        toolInfo5="extension is png."
        toolInfo6=" "
        if mb[0]==1:
            tool="Save"

    #sticker selection
    if izayaRect.collidepoint(mx,my):
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Izaya"
    if shizuoRect.collidepoint(mx,my) and mb[0]==1:
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Shizuo"
    if kidaRect.collidepoint(mx,my) and mb[0]==1:
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Kida"
    if mikadoRect.collidepoint(mx,my):
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Mikado"
    if anriRect.collidepoint(mx,my):
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Anri"
    if kadotaRect.collidepoint(mx,my):
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Kadota"
    if celtyRect.collidepoint(mx,my):
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Celty"
    if shinraRect.collidepoint(mx,my):
        toolInfo1="Click on the canvas"
        toolInfo2="to paste the stamp."
        toolInfo3=" "
        toolInfo4=" "
        toolInfo5=" "
        toolInfo6=" "
        if mb[0]==1:
            tool="Shinra"



    
    #blitting tool icons
    screen.blit(pencilIcon,(30,40))
    screen.blit(eraserIcon,(110,40))
    screen.blit(paintbrushIcon,(30,120))
    screen.blit(dropperIcon,(110,120))
    screen.blit(recttoolIcon,(30,200))
    screen.blit(ellipseIcon,(110,200))
    screen.blit(lineIcon,(30,280))
    screen.blit(spraypaintIcon,(105,275))
    screen.blit(fillIcon,(30,360))
    screen.blit(highlightIcon,(110,360))
    screen.blit(undoIcon,(25,435))
    screen.blit(redoIcon,(105,435))
    screen.blit(openIcon,(30,520))
    screen.blit(saveIcon,(110,520))

    screen.blit(paletteIcon,(580,775))

    #blitting sticker icons
    screen.blit(izayaIcon,(10,750))
    screen.blit(shizuoIcon,(151,750))
    screen.blit(kidaIcon,(292,750))
    screen.blit(mikadoIcon,(433,750))
    screen.blit(shinraIcon,(1132,750))
    screen.blit(celtyIcon,(997,750))
    screen.blit(kadotaIcon,(856,750))
    screen.blit(anriIcon,(725,750))

    
        

       
    ########################################################
    #select (change) colour
    if paletteRect.collidepoint(mx,my) and mb[0]==1:
        col=screen.get_at((mx,my))
    draw.ellipse(screen,col,paletteRect,4)    

    ########################################################
    #using the tool
    
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        draw.ellipse(screen,col,paletteRect,2)
        screen.set_clip(canvasRect)
        #only allows the canvas to be modified
        
        if tool=="Pencil":
            
            draw.aaline(screen,col,(omx,omy),(mx,my),sz)   #draws smooth line for pencil
        if tool=="Eraser":
            draw.rect(screen,RED,eraserRect,2)
            if mb[0]==1:
                dx=mx-omx  #base
                dy=my-omy  #height
                dist=int(sqrt(dx**2+dy**2))  #distance (hypotenuse)
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)    #horizontal shift (run),creates new x pos 
                dotY=int(omy+i*dy/dist)    #vertical shift (rise),creates new x pos 
                draw.circle(screen,WHITE,(dotX,dotY),sz)#draws the new x and y pos along the distance   
           
        if tool=="Paintbrush":
            if mb[0]==1:
                dx=mx-omx   #base of triangle
                dy=my-omy   #height of triangle
                dist=int(sqrt(dx**2+dy**2))   #distance (hypotense)
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)    #horizontal shift (run), creates new x pos 
                dotY=int(omy+i*dy/dist)    #vertical shift (rise), creates new y pos
                draw.circle(screen,col,(dotX,dotY),sz) #draws the new x and y pos along the distance  

        if tool=="Dropper":
            col=screen.get_at((mx,my))  #gets screen colour
                       
 

        if tool=="Spraypaint":
            for i in range(int(sz**1.5)):  #sz**1.5 increases the speed of dots
                px=randint(-sz,sz) #finds random spots from -sz to sz for x coordinate
                py=randint(-sz,sz) #finds random spots from -sz to sz for y coordinate
                if px**2+py**2<sz**2:  #if px and py are within hypotenuse, 
                    screen.set_at((mx+px,my+py),col) #sets pos of px and py

        if tool=="Line":
            screen.blit(back,(0,0))
            draw.line(screen,col,(sx,sy),(mx,my),sz) #draws a line from where you click (sx,sy) to your current mouse position
                

        if tool=="Rectangle":
            if sz>1:
                if mx>sx and my>sy:  #for rectangle being drawn top to bottom
                    hSz=sz/2  #half of the size
                    screen.blit(back,(0,0))
                    draw.line(screen,col,(sx,sy),(sx,my),sz)    #drawing 4 separate lines to fix
                    draw.line(screen,col,(mx,sy),(mx,my),sz)
                    draw.line(screen,col,(sx-hSz+1,sy),(mx+hSz,sy),sz)  #unfilled edges of rectangle
                    draw.line(screen,col,(sx-hSz+1,my),(mx+hSz,my),sz)  

                if sx>mx and sy>my: #for rectangle being drawn bottom to top
                    hSz=sz/2
                    screen.blit(back,(0,0))
                    draw.line(screen,col,(sx,sy),(sx,my),sz)
                    draw.line(screen,col,(mx,sy),(mx,my),sz)
                    draw.line(screen,col,(sx+hSz,sy),(mx-hSz+1,sy),sz)
                    draw.line(screen,col,(sx+hSz,my),(mx-hSz+1,my),sz)
            if sz-1==0:
                screen.blit(back,(0,0))    #for the filled rectnalge
                draw.rect(screen,col,(sx,sy,mx-sx,my-sy),sz-1)  #draws an unfilled rectangle
        if tool=="Ellipse":
            screen.blit(back,(0,0))
            rect=Rect(sx,sy,mx-sx,my-sy) #mx-sx is the width  #my-sy is the height
            rect.normalize()   #turns any negative width/height and makes it positive
            if abs(mx-sx)>3 and abs(my-sy)>3: #the width can't be greater than the radius
                draw.ellipse(screen,col,rect,2)
            if sz-1==0:  #draws filled ellipse
                draw.ellipse(screen,col,rect,0)
            
        if tool=="Highlight":
            screen.blit(highlightHead,(mx-10,my-10))
            myClock.tick(50)
        if tool=="Fill":
            if mb[0]==1:  #when left clicked 
                mx,my=mouse.get_pos()
                rc=screen.get_at((mx,my))  #gets the colour of pixel where the user clicked  
                spots=[(mx,my)]  #the point clicked is part of the spots list
                while len(spots)>0:  #when the spots list has at least one element 
                    newSpots=[] #list of new spots
                    for fx,fy in spots:
                        if 180<fx<1100 and 30<fy<730 and screen.get_at((fx,fy))==rc:   #if fx and fy are within the range of the canvas
                            screen.set_at((fx,fy),col)                  #and the colour of the pixel of fx,fy is the same colour as

                                                             #the inital one selected earlier, then begin to fill the area 
                           
                                         #right    #left      #down    #up
                            newSpots+=[(fx+1,fy),(fx-1,fy),(fx,fy+1),(fx,fy-1)]  #these are the 4 points we fill
                                                             #from the initial point
                        spots=newSpots #each time, from the newSpots, they become spots and the right, left, up and down of
                                    #these points are counted as newSpots and we colour in those pixels     
        
            tool="Pencil"
            
        #using the stamps

        if tool=="Izaya":
            screen.blit(back,(0,0))
            screen.blit(izayaIcon,(mx-69,my-95))
        if tool=="Shizuo":
            screen.blit(back,(0,0))
            screen.blit(shizuoIcon,(mx-69,my-95))
        if tool=="Kida":
            screen.blit(back,(0,0))
            screen.blit(kidaIcon,(mx-69,my-95))
        if tool=="Mikado":
            screen.blit(back,(0,0))
            screen.blit(mikadoIcon,(mx-69,my-95))
        if tool=="Anri":
            screen.blit(back,(0,0))
            screen.blit(anriIcon,(mx-69,my-95))
        if tool=="Kadota":
            screen.blit(back,(0,0))
            screen.blit(kadotaIcon,(mx-69,my-95))
        if tool=="Celty":
            screen.blit(back,(0,0))
            screen.blit(celtyIcon,(mx-69,my-95))
        if tool=="Shinra":
            screen.blit(back,(0,0))
            screen.blit(shinraIcon,(mx-69,my-95))

            
        screen.set_clip(None)
        
              
    ########################################################
    #opening the picture

    if openRect.collidepoint(mx,my) and mb[0]==1:
        try: #prevents crashing
            fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
            #asks the user to open a file with the following extensions
            screen.set_clip(canvasRect)  #clips image inside canvas if larger than canvas
            image=image.load(fname) #loading the image
            screen.blit(image,(130,48)) #blitting the image
            screen.set_clip(None)
                    
        except:
            pass


    if saveRect.collidepoint(mx,my) and mb[0]==1:
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            #asks the user to input file name they would like to save as

            image.save(screen.subsurface(canvasRect),fname) #saving the image
        except:
            pass #prevent crashing
        
    

    toolInfo="Tool: " + tool
    
    #rendering the text
    displayTool=szFont.render(toolInfo,True,BLACK)
    displayTool1=szFont.render(toolInfo1,True,BLACK)
    displayTool2=szFont.render(toolInfo2,True,BLACK)
    displayTool3=szFont.render(toolInfo3,True,BLACK)
    displayTool4=szFont.render(toolInfo4,True,BLACK)
    displayTool5=szFont.render(toolInfo5,True,BLACK)
    displayTool6=szFont.render(toolInfo6,True,BLACK)
    
    #blitting the tool information text
    screen.blit(displayTool,(20,620))
    screen.blit(displayTool1,(20,640))
    screen.blit(displayTool2,(20,650))
    screen.blit(displayTool3,(20,660))
    screen.blit(displayTool4,(20,670))
    screen.blit(displayTool5,(20,680))
    screen.blit(displayTool6,(20,690))
        

    omx,omy=mx,my  #for the paint brush and pencil tool
    display.flip()
















