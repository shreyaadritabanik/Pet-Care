from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
#HEALTH=5 IS BEST UPPER LEFT SHOWS HEALTH BAR. HUNGER AND SLEEP CAN EFFECT HEALTH.
#HUNGRY AFTER FIRST 9 SECONDS.hunger increases by 1 after every 6 seconds and extremely hungry when hunger is 11
cat_x = 0.0
cat_y = -50
xaxis= 300
yaxis =300
food =[]
food_pan_empty = False
eating = False
nose = (0,0)
hungry=10
health =5
unhappy = False
food.append((233, -265))
food.append((253, -265))
food.append((243, -265))
food.append((263, -265))
food.append((273, -265))
food.append((283, -265))
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
    global cat_x, cat_y, eating, nose, unhappy
    glColor3f(0, 0, 0)
    
    # Head
    glPointSize(1.5)
    circle(40, (cat_x, cat_y-175))
    glPointSize(4)
    # Eyes
    
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

    #mouth
    glColor3f(0,0,0)
    if eating==False and unhappy==False:
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
def draw_foodpan():
    global food_pan_empty, food
    glPointSize(4)
    glColor3f(1,0.2,0.2)
    draw_line(220.0 ,-270.0,294.0 ,-270.0) #220,294
    draw_line(234.0 ,-289.0,281.0, -289.0)
    draw_line(220.0 ,-270.0,234.0 ,-289.0)
    draw_line(281.0, -289.0,294.0 ,-270.0)
    glPointSize(3)
    glColor3f(0.26,0.09,0.09) 
    for item in food:
        circle(4, (item[0], item[1]))
def healthbar():
    global health
    a=-270
    b=270
    c=20
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
    draw_cat()
    draw_foodpan()
    healthbar()
    if health<=0 and unhappy==False:
        print("!!!Your pet is unhappy!!!")
        unhappy=True
    elif health>0:
        unhappy=False    
    glutSwapBuffers()

def mouseFunc(button, state, x, y):
    global food_pan_empty, food, eating, cat_x,cat_y, nose, hungry, health, unhappy
    nose=(cat_x,cat_y-195)
    a =x-(600/2)
    b = (600 /2)-y
    if 220.0 <= a <= 294.0 and -289.0 <= b <= -270.0 and 170<=cat_x<=230:
        
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if not food_pan_empty:
                if len(food) > 1:
                    eating=True
                    food.pop()
                    hungry=max(0,hungry-1)
                    health+=1
                    health=min(health,4)
                    if hungry==0:
                        health=5
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
                  
                food.append((233, -265))
                food.append((253, -265))
                food.append((243, -265))
                food.append((263, -265))
                food.append((273, -265))
                food.append((283, -265))
                food.append((237, -255))
                food.append((257, -255))
                food.append((247, -255))
                food.append((267, -255))
                food.append((275, -255))
    else:
        eating=False            
    if nose[0]-3<a<nose[0]+3 and nose[1]-3<b<nose[1]+3:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            cat_y+=70
            glutTimerFunc(300, come_down, 0)
            
    glutPostRedisplay()
def come_down(val):
    global cat_y, hungry 
    cat_y-=70
    hungry+=0.5
    glutPostRedisplay()    
def specialKeyListener(key,x, y):
    global cat_x

    if key== GLUT_KEY_LEFT: 
        cat_x -= 10.0
    if key== GLUT_KEY_RIGHT:
        cat_x += 10.0

    glutPostRedisplay() 
def hungry_announce(val):
    global hungry,health
    glutTimerFunc(6000, hungry_announce, 0)
    if hungry==11:
        health-=1
        print("HUMGRYYY GIB FOOD")    
    elif hungry==0:
        print("I am full")
    hungry+=1
    hungry=min(11,hungry)   
    glutPostRedisplay()
def init():
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)        
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600,600) 
glutInitWindowPosition(600,0)
wind =glutCreateWindow(b"PET CARE") 
init()
glutDisplayFunc(showScreen)   
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseFunc)
glutTimerFunc(3000, hungry_announce, 0)
glutMainLoop()
