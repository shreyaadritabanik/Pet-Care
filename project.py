from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
width, height = 600, 600
#HEALTH=5 IS BEST UPPER LEFT SHOWS HEALTH BAR. HUNGER AND SLEEP CAN EFFECT HEALTH.
#HUNGRY AFTER FIRST 15 SECONDS.hunger increases by 1 after every 6 seconds and extremely hungry when hunger is 11
xaxis= width/2
yaxis =height/2
cat_x = 0.0
cat_y = -50
fish_x = random.uniform(width-850, width - 350) #width-850
fish_y = -100
fish_xbutton = width -350
fish_ybutton = 170
food =[]
food_pan_empty = False
eating = False
nose = (0,0)
hungry=10
health =5
energy = 5
unhappy = False
sleep = False
day = 1
d2n = True
n2d = False
play = False
ballx=-280
ballbutton = -280
ballbuttonON = False
fishON = False
fishgamepoint = 0
goal=True
fireworkCircleRadius = 0.5
fireworksCircleSpeed = 6
fireworksCircleColor = [1,0,0]
firework = False
fireworkLst = []
food.append((xaxis-67, -(yaxis-35)))
food.append((xaxis-57, -(yaxis-35)))
food.append((xaxis-47, -(yaxis-35)))
food.append((xaxis-37, -(yaxis-35)))
food.append((xaxis-27, -(yaxis-35)))
food.append((xaxis-17, -(yaxis-35)))
def findzone(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy):
        if(dx>=0 and dy>=0):
            zone=0
        elif(dx<=0 and dy>=0):
            zone=3
        elif(dx<=0 and dy<=0):
            zone=4
        elif(dx>=0 and dy<=0):
            zone=7
    else:
        if(dx>=0 and dy>=0):
            zone=1
        elif(dx<=0 and dy>=0):
            zone=2
        elif(dx<=0 and dy<=0):
            zone=5
        elif(dx>=0 and dy<=0):
            zone=6
    return zone        
def zone0(zone,x,y):
    if zone==0:
        x1=x
        y1=y
    elif zone==1: 
        x1=y 
        y1=x 
    elif zone==2:    
        x1=y 
        y1=-x    
    elif zone==3: 
        x1=-x
        y1=y
    elif zone==4: 
        x1=-x
        y1=-y
    elif zone==5: 
        x1=-y
        y1=-x
    elif zone==6:    
        x1=-y
        y1=x    
    elif zone==7:     
        x1=x
        y1=-y
    return (x1,y1)
def originalzone(zone,x,y):
    if zone==0:
        x1=x
        y1=y
    elif zone==1:
        x1=y
        y1=x
    elif zone==2:
        x1=-y
        y1=x
    elif zone==3:
        x1=-x
        y1=y
    elif zone==4:
        x1=-x
        y1=-y
    elif zone==5:
        x1=-y
        y1=-x
    elif zone==6:
        x1=y
        y1=-x
    elif zone==7:
        x1=x
        y1=-y
    return (x1,y1)            
def draw_line(x1,y1,x2,y2):
    global xaxis,yaxis
    zone=findzone(x1,y1,x2,y2)
    x1,y1=zone0(zone,x1,y1)
    x2,y2=zone0(zone,x2,y2)
    dx=x2 -x1
    dy=y2 -y1
    d= 2*dy -dx
    x=x1
    y=y1
    glBegin(GL_POINTS)
    while x <x2:
        xo,yo= originalzone(zone,x,y)
        glVertex2f(xo/xaxis, yo/yaxis) #
        x +=1
        if d<0:
            d+=2*dy
        else:
            d+=2*(dy- dx)
            y+=1
    glEnd()
def circle(radius,center):
    d=1-radius
    x=0
    y=radius 
    circlepoints(x,y,center)
    while(x<y):
        if(d<0):
            d=d+ 2*x + 3
            x+=1
        else:
            d= d+ 2*x - 2*y + 5 
            x+=1
            y-=1
        circlepoints(x,y,center)       
def circlepoints(x,y,center):
    global xaxis, yaxis
    glBegin(GL_POINTS)
    
    x0=x/xaxis
    y0=y/yaxis
    ax=center[0]/xaxis
    ay=center[1]/yaxis
    glVertex2f(x0+ax,y0+ay)
    glVertex2f(y0+ax,x0+ay)
    glVertex2f(y0+ax,-x0+ay)
    glVertex2f(x0+ax,-y0+ay)
    glVertex2f(-x0+ax,-y0+ay)
    glVertex2f(-y0+ax,-x0+ay)
    glVertex2f(-y0+ax,x0+ay)
    glVertex2f(-x0+ax,y0+ay)
    glEnd()

def draw_cat():
    global cat_x, cat_y, eating, nose, unhappy, sleep
    glColor3f(0, 0, 0)
    
    # Head
    glPointSize(1.5)
    circle(40, (cat_x, cat_y-175))
    glPointSize(4)
    # Eyes
    if firework == True:
        glPointSize(2)
        draw_line(cat_x+8,cat_y-182, cat_x+13,cat_y-173)
        draw_line(cat_x+13,cat_y-175, cat_x+16,cat_y-183)

        draw_line(cat_x-8,cat_y-182, cat_x-13,cat_y-173)
        draw_line(cat_x-13,cat_y-173, cat_x-18,cat_y-182)
    elif sleep == False:
        glColor3f(0, 0, 0)  # Black color for the eyes
        circle(3, (cat_x-10, cat_y-182))
        circle(3, (cat_x-10, cat_y-179))
        circle(3, (cat_x-10, cat_y-175))
        circle(2, (cat_x-10, cat_y-172))
        circle(1, (cat_x-10, cat_y-171))
        circle(0.5, (cat_x-10, cat_y-170))
        circle(2, (cat_x-10, cat_y-185))
        circle(1, (cat_x-10, cat_y-187))
        

        circle(3, (cat_x+10, cat_y-182))
        circle(3, (cat_x+10, cat_y-179))
        circle(3, (cat_x+10, cat_y-175))
        circle(2, (cat_x+10, cat_y-172))
        circle(1, (cat_x+10, cat_y-171))
        circle(0.5, (cat_x+10, cat_y-170))
        circle(2, (cat_x+10, cat_y-185))
        circle(1, (cat_x+10, cat_y-187))

        glColor3f(1,1,1)
        glPointSize(2)
        circle(1, (cat_x-8, cat_y-185))
        circle(1, (cat_x+12, cat_y-185))
    else: #sleeepy eyes
        glPointSize(2)
        draw_line(cat_x+8,cat_y-182, cat_x+14,cat_y-182)
        draw_line(cat_x-8,cat_y-182, cat_x-14,cat_y-182)
    # Nose
    glPointSize(4)
    glColor3f(1,0.8,0.8)  # Red color for the nose
    circle(2, (cat_x,cat_y-195))
    circle(1,(cat_x+3,cat_y-195))
    circle(1,(cat_x-3,cat_y-195))
    nose=(cat_x,cat_y-195)
   # body
    glPointSize(2)
    glColor3f(0,0,0)
    draw_line(cat_x-12,cat_y-215, cat_x-30, cat_y-240)
    draw_line(cat_x+12,cat_y-240, cat_x-30, cat_y-240)
    draw_line(cat_x+12,cat_y-240, cat_x+10, cat_y-215)

    #ears
    draw_line(cat_x-40,cat_y-162, cat_x-62, cat_y-127)
    draw_line(cat_x-17,cat_y-137, cat_x-43, cat_y-115)
    draw_line(cat_x-62, cat_y-127, cat_x-45, cat_y-115)
    draw_line(cat_x-62, cat_y-127, cat_x-49, cat_y-132)
    draw_line(cat_x-45, cat_y-115, cat_x-49, cat_y-132)
    draw_line(cat_x+14,cat_y-137, cat_x+59, cat_y-112)
    draw_line(cat_x+36,cat_y-158, cat_x+59, cat_y-112)
    glPointSize(5)
    glColor3f(1,0.8,0.8)
    draw_line(cat_x-34,cat_y-147, cat_x-38, cat_y-139)
    draw_line(cat_x-29,cat_y-143, cat_x-38, cat_y-139)
    draw_line(cat_x+28,cat_y-143, cat_x+38, cat_y-139)
    draw_line(cat_x+33,cat_y-147, cat_x+38, cat_y-139)
    #whiskers
    glColor3f(0.8, 0.4, 0)
    glPointSize(0.5)
    draw_line(cat_x - 10, cat_y - 193, cat_x -20, cat_y - 188)
    draw_line(cat_x - 10, cat_y - 195, cat_x -20, cat_y - 195)
    draw_line(cat_x - 10, cat_y - 197, cat_x -20, cat_y - 202)

    draw_line(cat_x + 10, cat_y - 193, cat_x +20, cat_y - 188)
    draw_line(cat_x + 10, cat_y - 195, cat_x +20, cat_y -195)
    draw_line(cat_x + 10, cat_y - 197, cat_x +20, cat_y - 202)

    #mouth
    glColor3f(0,0,0)
    if firework == True:
        glPointSize(2)
        circle(5,(cat_x,cat_y-205))
    elif eating==False and unhappy==False:
        glPointSize(0.5)
        draw_line(cat_x-10,cat_y-202, cat_x-5, cat_y-206)
        draw_line(cat_x-5, cat_y-206, cat_x-1, cat_y-201)
        draw_line(cat_x+5, cat_y-206, cat_x-1, cat_y-201)
        draw_line(cat_x+5, cat_y-206, cat_x+9, cat_y-202)
    elif eating==True and unhappy==False:
        glPointSize(1)
        circle(3,(cat_x,cat_y-205))
    elif unhappy==True:
        glPointSize(1)
        draw_line(cat_x-5, cat_y-206, cat_x-1, cat_y-201)
        draw_line(cat_x+5, cat_y-206, cat_x-1, cat_y-201)

    #tail
    glPointSize(2)
    glColor3f(0,0,0)
    draw_line(cat_x-30, cat_y-240, cat_x-50,cat_y-225)
    draw_line(cat_x-27, cat_y-235, cat_x-50,cat_y-215)
    draw_line(cat_x-50, cat_y-215, cat_x-55,cat_y-215)
    draw_line(cat_x-50, cat_y-225, cat_x-55,cat_y-230)
    glPointSize(7)
    circle(4, (cat_x-55, cat_y-222))

    #paws
    glPointSize(5)
    glColor3f(1,0.8,0.8)
    circle(3, (cat_x-17, cat_y-243))
    circle(3, (cat_x, cat_y-243))
def draw_foodpan():
    global food_pan_empty, food, play, xaxis, yaxis 
    if play == False:
        glPointSize(4)
        glColor3f(1,0.2,0.2)
        draw_line((xaxis-80) ,-(yaxis-30),(xaxis-6),-(yaxis-30)) #220,294
        draw_line((xaxis-66) ,-(yaxis-11),(xaxis-20) ,-(yaxis-11)) #234.0 ,-289.0,281.0, -289.0
        draw_line((xaxis-80) ,-(yaxis-30), (xaxis-66),-(yaxis-11)) #220.0 ,-270.0,234.0 ,-289.0
        draw_line((xaxis-20), -(yaxis-11), (xaxis-6), -(yaxis-30)  )#281.0, -289.0,294.0 ,-270.0
        glPointSize(3)
        glColor3f(0.26,0.09,0.09) 
        for item in food:
            circle(4, (item[0], item[1]))
def draw_bed():
    global play
    if play == False:
        glPointSize(5)
        glColor3f(0,0,0)
        # draw_line(xaxis - 590, yaxis -550, xaxis-500, yaxis-550)
        draw_line(xaxis - 590, yaxis -580, xaxis-500, yaxis-580)
        draw_line(xaxis - 590, yaxis -550, xaxis-590, yaxis-590)
        draw_line(xaxis - 500, yaxis -580, xaxis-500, yaxis-590)
        glColor3f(.4,.2,0.05)
        draw_line(xaxis - 585, yaxis -575, xaxis-500, yaxis-575)
        #pillow
        glColor3f(.7,.2,0.05)
        glPointSize(3)
        circle(5, (xaxis-582, yaxis-567))
def draw_window():
    global day, play, n2d, d2n
    glColor3f(0,0,0)
    glPointSize(2)
    #window
    if play == False:
        draw_line(-width + 400, height - 400, width - 600, height-400)
        draw_line(-width + 400, height - 600, width - 600, height-600)
        draw_line(-width + 400, height - 400, -width + 400, height - 600)
        draw_line(width - 600, height-400, width - 600, height - 600)
        #sky
        if day > 0.9:
            glColor3f(0,0.7,1)
        else:
            g= max(0.1, day-0.4)
            b= max(0.1, day-0.2)
            glColor3f(0,g,b)
        glPointSize(198)
        draw_line(-width + 500, height - 500, width - 699, height-500)
        #sun
        if 0.4<day<=1: 
            h = height
            inc = 0
            if day == 1:
                glColor3f(1,1,0)
            elif 0.9 >= day > 0.4:
                glColor3f(day-.2,day-.2,0)
            if d2n == True and day < 1:
                h = height - (1-day)*200
            elif n2d == True and day < 1:
                h = height - (1-day)*200 + inc
                inc += 1
            glPointSize(5)
            circle(15, (-width + 450, h - 450))
            circle(10, (-width + 450, h - 450))
            circle(5, (-width + 450, h - 450))
            glPointSize(2)
            draw_line (-width + 425, h - 450, -width + 475, h-450)
            draw_line (-width + 450, h - 425, -width + 450, h-475)
            draw_line (-width + 435, h - 430, -width + 465, h - 470)
            draw_line(-width + 435, h - 470, -width + 465, h - 430)
       


    #PLAYROOM
    else: 
        draw_line(-width + 400, height - 400, width - 400, height-400)
        draw_line(-width + 400, height - 600, width - 400, height-600)
        draw_line(-width + 400, height - 400, -width + 400, height - 600)
        draw_line(width - 400, height-400, width - 400, height - 600)
        #sky
        if day > 0.9:
            glColor3f(0,0.7,1)
        else:
            g= max(0.1, day-0.4)
            b= max(0.1, day-0.2)
            glColor3f(0,g,b)
        glPointSize(198)
        draw_line(-width + 500, height - 500, width - 499, height-500)
        #sun
        if 0.4<day<=1: 
            h = height
            inc = 0
            if day == 1:
                glColor3f(1,1,0)
            elif 0.9 >= day > 0.4:
                glColor3f(day-.2,day-.2,0)
            if d2n == True and day < 1:
                h = height - (1-day)*200
            elif n2d == True and day < 1:
                h = height - (1-day)*200 + inc
                inc += 1
            glPointSize(5)
            circle(15, (-width + 450, h - 450))
            circle(10, (-width + 450, h - 450))
            circle(5, (-width + 450, h - 450))
            glPointSize(2)
            draw_line (-width + 425, h - 450, -width + 475, h-450)
            draw_line (-width + 450, h - 425, -width + 450, h-475)
            draw_line (-width + 435, h - 430, -width + 465, h - 470)
            draw_line(-width + 435, h - 470, -width + 465, h - 430)
        #window cross
        
def windowcross():
    #window cross
    if play == False:
        glColor3f(0,0,0)
        glPointSize(1)
        draw_line(width -700, height - 400, width - 700, height-600)
        draw_line(-width + 400, height - 500, width - 600, height-500)
    else:
        glColor3f(0,0,0)
        glPointSize(1)
        draw_line(width - 600, height-402, width - 600, height - 598)
        draw_line(width -700, height - 402, width - 700, height-598)
        draw_line(width -700, height - 402, width - 700, height-598)
        draw_line(-width + 400, height - 502, width - 400, height-502)
        draw_line(width -500, height - 402, width - 500, height-598)
def draw_fish():
    if play == True and fishON == True:
        global fish_x, fish_y
        glPointSize(2)
        glColor3f(0.0, 0.0, 1.0)  # Set color to blue
        draw_line(fish_x - 15, fish_y, fish_x + 15, fish_y)
        draw_line(fish_x - 15, fish_y-20, fish_x + 15, fish_y-20)
        draw_line(fish_x - 15, fish_y, fish_x - 27, fish_y - 10)
        draw_line(fish_x - 15, fish_y-20, fish_x - 27, fish_y - 10)
        draw_line(fish_x + 15, fish_y, fish_x + 40, fish_y - 15)
        draw_line(fish_x + 15, fish_y-20, fish_x + 40, fish_y-5)
        draw_line(fish_x + 40, fish_y - 15, fish_x + 40, fish_y-5)
        #eye
        circle(1, (fish_x - 12, fish_y -7))
    
def playbutton():
    global play, fish_xbutton, fish_ybutton
    glColor3f(0,0.4,1)
    glPointSize(2)
    #box
    draw_line(width - 320, height - 350, width - 370, height- 350)
    draw_line(width - 320, height - 370, width - 370, height- 370)
    draw_line(width - 315, height - 365, width-315, height-355)
    draw_line(width - 375, height - 365, width-375, height-355)

    draw_line(width - 370, height - 350, width-375, height-355)
    draw_line(width - 370, height- 370, width-375, height-365)
    draw_line(width - 320, height - 350, width-315, height-355)
    draw_line(width - 320, height - 370, width - 315, height - 365)
    
    #play
    glPointSize(2)
    if play == False:
        #P
        draw_line(width - 365, height - 365, width-365, height-355)
        draw_line(width - 361, height - 361, width-361, height-356)
        draw_line(width - 365, height - 355,width - 361, height - 356)
        draw_line(width - 361, height - 361, width-365, height-361)
        #L
        draw_line(width - 353, height - 365, width-353, height-355)
        draw_line(width - 353, height - 365, width-348, height - 365)
        #A
        draw_line(width - 337, height - 365, width-340, height-355) #\
        draw_line(width - 343, height - 365, width-340, height-354) #/
        draw_line(width - 337, height-362, width-342,height-362)
        #Y
        draw_line(width - 330, height - 362, width-333, height-355) #-10
        draw_line(width - 330, height - 362, width-327, height-355)
        draw_line(width - 330, height - 362, width-330, height-366)
    else:
        #stop
        # S
        draw_line(width - 365, height - 355, width - 360, height-355)
        draw_line(width - 365, height - 360, width - 360, height-360)
        draw_line(width - 365, height - 365, width - 360, height-365)
        draw_line(width - 365, height - 355, width - 365, height-360)
        draw_line(width - 360, height-360, width - 360, height-365)
        #T
        draw_line(width - 357, height - 355, width - 350, height-355)
        draw_line(width - 354, height - 355, width - 354, height-365)
        #O
        circle(4.3, (width-343, height-360))
        #P
        draw_line(width - 335, height - 365, width-335, height-355)
        draw_line(width - 331, height - 361, width-331, height-356)
        draw_line(width - 335, height - 355,width - 331, height - 356)
        draw_line(width - 331, height - 361, width-335, height-361)
        #ballbutton
        if ballbuttonON == False:
            glPointSize(4)
            glColor3f(1,0,0)
            circle(16,(-ballbutton-30,200))
            glColor3f(1,0,1)
            circle(11,(-ballbutton-30,200))
            glColor3f(1,0,0)
            circle(7,(-ballbutton-30,200))
            circle(4,(-ballbutton-30,200))
        if ballbuttonON == True:
            glPointSize(8)
            glColor3f(1,0,0)
            circle(16,(-ballbutton-30,200))
            circle(12,(-ballbutton-30,200))
            circle(8,(-ballbutton-30,200))
            circle(5,(-ballbutton-30,200))
        #fishbutton
        if fishON == False:
            glPointSize(2)
            glColor3f(0.0, 0.0, 1.0)  # Set color to blue
            draw_line(fish_xbutton - 15, fish_ybutton, fish_xbutton + 15, fish_ybutton)
            draw_line(fish_xbutton - 15, fish_ybutton-20, fish_xbutton + 15, fish_ybutton-20)
            draw_line(fish_xbutton - 15, fish_ybutton, fish_xbutton - 27, fish_ybutton - 10)
            draw_line(fish_xbutton - 15, fish_ybutton-20, fish_xbutton - 27, fish_ybutton - 10)
            draw_line(fish_xbutton + 15, fish_ybutton, fish_xbutton + 40, fish_ybutton - 15)
            draw_line(fish_xbutton + 15, fish_ybutton-20, fish_xbutton + 40, fish_ybutton-5)
            draw_line(fish_xbutton + 40, fish_ybutton - 15, fish_xbutton + 40, fish_ybutton-5)
            #eye
            circle(1, (fish_xbutton - 12, fish_ybutton -7))
        if fishON == True:
            glPointSize(8)
            glColor3f(1,0,0)
            circle(16,(-ballbutton-30,150))
            circle(12,(-ballbutton-30,150))
            circle(8,(-ballbutton-30,150))
            circle(5,(-ballbutton-30,150))

def playroomtoys():
    #ball
    if ballbuttonON == True:
        glPointSize(4)
        glColor3f(1,0,0)
        circle(16,(ballx,-275))
        glColor3f(1,0,1)
        circle(11,(ballx,-275))
        glColor3f(1,0,0)
        circle(7,(ballx,-275))
        circle(4,(ballx,-275))
        #goalpost
        if goal==True:
            glColor3f(0,0,0)
            draw_line(290,-290,290,-220)
            draw_line(250,-280,250,-210)
            draw_line(290,-220,250,-210)
        else:
            glColor3f(0,0,0)
            draw_line(-290,-290,-290,-220)
            draw_line(-250,-280,-250,-210)
            draw_line(-290,-220,-250,-210)
        
def fcircle(radius,center): #(5,(1,2))
    for _ in range(10):
        d=1-radius
        x=0
        y=radius 
        
        glPointSize(3)
        fcirclepoints(x,y,center)
        while(x<y):
            
                if(d<0):
                    d=d+ 2*x + 3
                    x+=1
                else:
                    d= d+ 2*x - 2*y + 5 
                    x+=1
                    y-=1
                if random.random() < 0.1:
                    fcirclepoints(x,y,center)
        radius -= 30
def fcirclepoints(x,y,center):
    global xaxis, yaxis, width, height
    glBegin(GL_POINTS)
    x0=x/xaxis
    y0=y/yaxis
    ax=center[0]/xaxis
    ay=center[1]/yaxis
    if play and (
        x0 + ax <= width - 400
        # and height - 800 <= y0 + ay <= height - 400
    ):
        # Perform transformations only for points within the window boundaries

        glVertex2f(x0 + ax, y0 + ay)
        glVertex2f(y0 + ax, x0 + ay)
        glVertex2f(y0 + ax, -x0 + ay)
        glVertex2f(x0 + ax, -y0 + ay)
        glVertex2f(-x0 + ax, -y0 + ay)
        glVertex2f(-y0 + ax, -x0 + ay)
        glVertex2f(-y0 + ax, x0 + ay)
        glVertex2f(-x0 + ax, y0 + ay)
    glEnd()     
     
def fireworkDisplay():
    global firework, fireworkLst, fireworkCircleRadius
    if play == True and len(fireworkLst) > 0:
        firework = True
    else:
        firework = False
    for i in fireworkLst:
        glColor3f(random.random(), random.random(), random.random()) 
        fcircle(i[2], (i[0], i[1]))
        if i[2] > 2 * height:
            fireworkLst.remove(i)
    #print(fireworkLst)
def toclear():
    glColor3f(1,1,1)
    glPointSize(200)
    draw_line(width-300, height+700, width-300, height-900)
    glPointSize(100)
    draw_line(width-850, height+700, width-850, height-900)
    glPointSize(300)
    draw_line(width-850, height-750, width, height-750)
    glPointSize(200)
    draw_line(width-850, height-300, width, height-300)
def healthbar():
    global health
    a=-(xaxis-50)
    b=yaxis-30
    c=20
    glPointSize(4)
    glColor3f(1,0,0)
    draw_line(-285,275,-280,263)
    draw_line(-275,275,-280,263)
    circle(1,(-280,270))
    circle(1,(-285,273))
    circle(1,(-275,273))
    draw_line(-286,275,-280,263)
    draw_line(-274,275,-280,263)

    glPointSize(2)
    glColor3f(0,0,0)
    circle(12,(-280,270))
    draw_line(-270,280,-155,280)
    draw_line(-270,260,-155,260)
    draw_line(-155,280,-155,260)
    glPointSize(6)
    glColor3f(0.4,0.8,0.4)
    health=max(0,health)
    for i in range(health):
        circle(5,(a,b)) 
        a+=c
def showScreen():
    global health,unhappy
    glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_window()
    fireworkDisplay()
    toclear()
    draw_cat()
    draw_foodpan()
    healthbar()
    draw_bed()
    playbutton()
    windowcross()
    draw_fish()
    
    
    if play==True and sleep==False:
        playroomtoys()
    if health<=0 and unhappy==False:
        print("!!!Your pet is unhappy!!!")
        unhappy=True
    elif health>0:
        unhappy=False    
    glutSwapBuffers()
def mouseFunc(button, state, x, y):
    global fishgamepoint, fish_x, fish_y, fishON, ballbuttonON, ballbutton, firework, fireworksCircleSpeed, fireworkCircleRadius, play, food_pan_empty, food, eating, cat_x,cat_y, nose, hungry, health, unhappy, sleep, day
    nose=(cat_x,cat_y-195)
    a = x-(600/2) 
    b = (600 /2)-y
    zzz = False
    if play == True and width-370<=a<=width-320 and height-410<=b<=height-390:
        if fishON == False and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == False:
            ballbuttonON = True
        elif fishON == False and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == True:
            ballbuttonON = False

    if play == True and width-370<=a<=width-320 and height-460<=b<=height-420:
        if fishON == False and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == False:
            fishON = True
        elif fishON == True and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and ballbuttonON == False:
            fishON = False
            print("Fishing Game Final Score: ",fishgamepoint)
            fishgamepoint = 0
           
    #eat or not eat xaxis = 300, yaxis = 300
    if play == False and (xaxis-80) <= a <= (xaxis-6) and -(yaxis-11) <= b <= -(yaxis-30)  and 170<=cat_x<=230:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if not food_pan_empty:
                if len(food) > 1 and hungry != 0:
                    eating=True
                    food.pop()
                    hungry=max(0,hungry-1)
                    health+=1
                    health=min(health,4)
                    if hungry==0:
                        health=5
                elif len(food) > 1 and hungry == 0: #moiukh
                    print("I am not hungry anymore.")
                elif len(food)==1:
                    food.pop()
                    hungry=max(0,hungry-1)
                    print("Oh no! Refill food")
                    food_pan_empty = True
                    eating=False
                elif len(food)==0:
                    food_pan_empty = True
                    eating=False
            else:
                food_pan_empty = False
                food.append((xaxis-67, -(yaxis-35)))
                food.append((xaxis-57, -(yaxis-35)))
                food.append((xaxis-47, -(yaxis-35)))
                food.append((xaxis-37, -(yaxis-35)))
                food.append((xaxis-27, -(yaxis-35)))
                food.append((xaxis-17, -(yaxis-35)))  
                food.append((xaxis-63, -(yaxis-45)))
                food.append((xaxis-53, -(yaxis-45)))
                food.append((xaxis-43, -(yaxis-45)))
                food.append((xaxis-33, -(yaxis-45)))
                food.append((xaxis-23, -(yaxis-45)))

    else:
        eating=False    

    if play == False and 0<=x<=100 and height-40<=y<=height and -xaxis+60 <=cat_x<-xaxis+160:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if day > 0.4 and sleep == False:
                print("It's still day! You should playy!")
            elif unhappy == True:
                print("Eat first.")
            else:
                zzz = True
        if zzz == True and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and sleep == False:
            sleep = True
            cat_y += 20
            cat_x = -230
        elif sleep == True and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            sleep = False
            cat_y -= 20
            if day <= 0.4:
                print('Sleep some more.')
    
    if width-370<=a<=width-320 and height-370<=b<=height-350:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if play == False:
                if unhappy == False:
                    if sleep==True:
                        print("To play, you need energy. Finish sleeping.")
                    else:
                        play = True
                else:
                    print("To play, you need to eat first.")
            else:
                play = False
                if fishON == True:
                    print("Fishing game Final Score: ", fishgamepoint)
                    fishON = False
                ballbuttonON = False
    
    


    #fireworks
    if play == True and button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
       if  -width + 400 <= a <= width - 400 and height-600<=b<=height-400:
            fireworkLst.append([a, b, 3]) #initial radius 3
    glutIdleFunc(fireworks_animate)
    
def fireworks_animate():
    global fireworkCircleRadius, fireworksCircleSpeed

    if len(fireworkLst) > 0:
        for i in range(len(fireworkLst)):
            fireworkLst[i][2] += fireworksCircleSpeed
        glutPostRedisplay()

def come_down(val):
    global cat_y, hungry 
    if cat_y > -50:
        cat_y-=70
    hungry+=0.5
    glutPostRedisplay()    
def specialKeyListener(key,x, y):
    global sleep, cat_x, cat_y, fish_x, fish_y, fishON, fishgamepoint

    if key== GLUT_KEY_LEFT and cat_x >= -xaxis+62 and sleep == False:
        cat_x -= 10.0
    if key== GLUT_KEY_RIGHT and cat_x <= xaxis-62 and sleep == False:
        cat_x += 10.0
    if sleep == False and key == GLUT_KEY_UP:
        if cat_y < 20:
            cat_y+=70
        glutTimerFunc(300, come_down, 0)
    if fishON == True:
        if cat_x-62<=fish_x+40 and cat_y-127 >=fish_y-20:
            fishgamepoint += 1
            print("point: ", fishgamepoint)
            fish_x = random.uniform(width-850, width - 350) #width-850
            fish_y = -100

    glutPostRedisplay() 
def keyboardListener(key, x,y):
    global ballx,cat_x,goal
    if play==True and key== b'w' and abs(cat_x-ballx)<=40:
        ballx+=40
        if ballx>270:
            ballx=280
            goal=False
            print("Yay goal!")
    if play==True and key== b'q' and abs(cat_x-ballx)<=40:     
        ballx-=40
        if ballx<-270:
            ballx=-280  
            goal=True 
            print("Yay goal!")
        
          
    glutPostRedisplay()         
def hungry_announce(val):
    global hungry,health, sleep
    glutTimerFunc(6000, hungry_announce, 0)
    if sleep == False:
        if hungry==11 and play==False:
            health-=1
            print("I am hungry. Let's go eat")   
        elif hungry==11 and play==True:
            health-=1
            if health <= 2:
                print("Enough playing. Let's go eat first")
        # elif hungry==0:
        #     print("I am full")
        hungry+=0.5
        hungry=min(11,hungry)   
    glutPostRedisplay()

def sleep_announce(val):
    global sleep, hungry, day
    glutTimerFunc(6000, sleep_announce, 0)
    
    glutPostRedisplay()   
def day_announce(val):
    global day, d2n, n2d, sleep
    glutTimerFunc(6000, day_announce, 0)
    if day <= 0.1:
        n2d = True
        d2n = False
    if day >=1:
        d2n = True
        n2d = False
    if n2d == True and day < 1:
        day += 0.1
    elif d2n == True and day >= 0.1:
        day -= 0.1
    if day <=0.4 and sleep == False:
        print("Time to sleep.")
    if day >=0.7 and sleep == True:
        print('Time to wakey wakey.')
    glutPostRedisplay()


def init():
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)        
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height) 
glutInitWindowPosition(0,0)
wind =glutCreateWindow(b"PET CARE") 
init()
glutDisplayFunc(showScreen) 
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseFunc)
glutKeyboardFunc(keyboardListener) 
glutTimerFunc(3000, hungry_announce, 0)
glutTimerFunc(3000, sleep_announce, 0)
glutTimerFunc(3000, day_announce, 0)
glutTimerFunc(20, fireworks_animate, 0)
glutMainLoop()
