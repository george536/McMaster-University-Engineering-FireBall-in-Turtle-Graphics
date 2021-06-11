#Name: George Yazji
#MacId: yazjig
#McMaster Fireball Design
##29/11/2020
import turtle
t=turtle.Pen()
def draw(angle,distance):   #The main function used in the program, it basically draws lines up to a destination and returns the position of that point
    t.color("grey")
    t.right(angle)
    t.forward(distance)
    position=t.position()
    t.color("grey")
    t.backward(distance)
    t.left(angle)
    return position

def outer_circle():   #function that draws the outer border of the circle starting from center
    for i in range(0,695,1):
        position=draw(-i,(i/4.8))
        positions1.append(position)
 
def inner_circle():   #function that draws the inner border of the circle starting from center
    for i in range(0,1055,1):
        position=draw(-i,(i/6.5))
        positions2.append(position)

def curved_lines(starting_angle,Finishing_angle,starting_distnace,middle_angle,min_angle,mode):  #function that draws all the curved shapes on the sides of the fireball
    def first_part(starting_angle,starting_distnace,middle_angle): 
        ang=starting_angle
        x=starting_distnace
        while ang<=middle_angle:
            position=draw(ang,x)
            outer_border.append(position)
            ang+=0.5
            x+=2
        return x
    def second_part(middle_angle,min_angle,distance):
        x=distance
        ang=middle_angle
        while ang>=min_angle:
            position=draw(ang,x)
            outer_border.append(position)
            ang-=0.5
            x-=5
        return x
    def third_part(starting_distnace,min_angle,distance,Finishing_angle):
        x=distance
        ang=min_angle
        while ang<=Finishing_angle and x>=starting_distnace:
            position=draw(ang,x)
            outer_border.append(position)
            ang+=0.5
            x-=5
    if mode=="normal":  #This indicates that these functions above will be excuted in order to get the most common curved shape around the fireball
        distance=first_part(starting_angle,starting_distnace,middle_angle)
        distance=second_part(middle_angle,min_angle,distance)
        third_part(starting_distnace,min_angle,distance,Finishing_angle)

    elif mode=="reverse1" or mode=="side1" or mode=="side2":  #This parts draws the previous hsape reversed and the two shapes on right side, one is the reverse of the other
        def third_part0(starting_angle,starting_distnace,Finishing_angle,mid_angle):
            x=starting_distnace
            ang=starting_angle
            if mode=="reverse1":
                while ang<=mid_angle:
                    position=draw(ang,x)
                    outer_border.append(position)
                    ang+=0.5
                    x+=5
            elif mode=="side1":
                x=starting_distnace-20
                while ang<=mid_angle:
                    position=draw(ang,x)
                    outer_border.append(position)
                    ang+=0.5
                    x+=1
            elif mode=="side2":
                x=starting_distnace-20
                while ang>=mid_angle:
                    position=draw(ang,x)
                    temp.append(position)
                    ang-=0.5
                    x+=1.3
            return x

        def second_part0(mid_angle,max_angle,distance):
            x=distance
            ang=mid_angle
            if mode=="reverse1":
                while ang>=max_angle:
                    position=draw(ang,x)
                    outer_border.append(position)
                    ang-=0.5
                    x+=5
            elif mode=="side1":
                 while ang>=max_angle:
                    position=draw(ang,x)
                    outer_border.append(position)
                    ang-=0.5
                    x+=3
            elif mode=="side2":
                 while ang<=max_angle:
                    position=draw(ang,x)
                    temp.append(position)
                    ang+=0.5
                    x+=3
            return x

        def first_part0(max_angle,starting_distnace,distance):
            ang=max_angle
            x=distance
            if mode=="reverse1":
                while ang<=middle_angle and x>=starting_distnace:
                    position=draw(ang,x)
                    outer_border.append(position)
                    ang+=0.5
                    x-=2
            elif mode=="side1":
                x=distance+9
                while ang<=middle_angle and x>=starting_distnace:
                    position=draw(ang,x)
                    outer_border.append(position)
                    ang+=1
                    x-=5
            elif mode=="side2":
                x=distance+9
                while ang<=middle_angle and x>=starting_distnace:
                    position=draw(ang,x)
                    temp.append(position)
                    ang-=1
                    x-=5
        if mode=="reverse1":
            mid_angle=starting_angle-((starting_angle-Finishing_angle)/4)
            max_angle=starting_angle+7
        elif mode=="side1":
            mid_angle=starting_angle-(3*(starting_angle-Finishing_angle)/4)
            max_angle=mid_angle-2
        elif mode=="side2":
            mid_angle=starting_angle-(3*(starting_angle-Finishing_angle)/4)
            max_angle=mid_angle+2
        distance=third_part0(starting_angle,starting_distnace,Finishing_angle,mid_angle)
        distance=second_part0(mid_angle,max_angle,distance)
        first_part0(max_angle,starting_distnace,distance)
        
        if mode=="side2":  #this function is to get the list of positions in descending order
            i=0
            for i in range(len(temp)):
                outer_border.append(temp[(len(temp)-1)-i])
                i+=1
        
def bottom_circle(starting_angle,finishing_angle):  #this function draws the bottom outer semi circle peice of the fireball
    i=0
    for i in range(0,(starting_angle-finishing_angle)+1,1):
        position=draw(starting_angle-i,180)
        temp1.append(position)
    i=0
    for i in range(len(temp1)):  #this function is to get the list of positions in descending order
        outer_border.append(temp1[(len(temp1)-1)-i])
        i+=1

def color_area(positions1,positions2,temp2,temp3):   #This fucntion is set to color the inner space to match the background color of the design
    t.color("grey")
    t.width(0)
    t.goto(positions2[-1])
    i=0
    for i in range(len(positions1)):
        temp2.append(positions1[(len(positions1)-1)-i])
        i+=1
    i=0
    for i in range(len(positions2)):
        temp3.append(positions2[(len(positions2)-1)-i])
        i+=1
    i=0
    while i <(len(temp2)):
        t.width(4)
        t.color("black")
        t.goto(temp2[i])
        t.goto(temp3[i])
        i+=1
    i=0
    transition()
    while i<=360:
        t.width(4)
        t.color("black")
        t.goto(positions2[i])
        t.goto(0,-50)
        i+=1
   
def transition():  #A fucntion that moves the turtle to home position whicout drawing its track
    t.color("grey")
    t.width(0)
    t.penup()
    t.goto(0,-50)
    t.pendown()

def connect_dots(positions):  #function that draws the outer shape in red color after all base drawing is done
    t.color("grey")
    t.penup()
    t.goto(positions[0])
    t.pendown()
    t.color("red")
    for i in positions:
        t.width(4)
        t.color("red")
        t.goto(i)

def mcmaster_2024(): #this function is only used to write MCMASTER 2024, it is an extra step has nothing to deal with anything else in the program, everthing else is done using functions
    #M
    position=draw(-230,220)
    mcmaster.append(position)
    position=draw(-230,200)
    mcmaster.append(position)
    position=draw(-232,220)
    mcmaster.append(position)
    position=draw(-234,200)
    mcmaster.append(position)
    position=draw(-234,220)
    mcmaster.append(position)
    #C
    position=draw(-240,200)
    mcmaster.append(position)
    position=draw(-238,205)
    mcmaster.append(position)
    position=draw(-236,210)
    mcmaster.append(position)
    position=draw(-238,215)
    mcmaster.append(position)
    position=draw(-240,220)
    mcmaster.append(position)
    #M
    position=draw(-242,220)
    mcmaster.append(position)
    position=draw(-242,200)
    mcmaster.append(position)
    position=draw(-244,220)
    mcmaster.append(position)
    position=draw(-246,200)
    mcmaster.append(position)
    position=draw(-246,220)
    mcmaster.append(position)
    #A
    position=draw(-248,220)
    mcmaster.append(position)
    position=draw(-250,200)
    mcmaster.append(position)
    position=draw(-252,220)
    mcmaster.append(position)
    #S
    position=draw(-254,220)
    mcmaster.append(position)
    position=draw(-256,213)
    mcmaster.append(position)
    position=draw(-254,207)
    mcmaster.append(position)
    position=draw(-256,200)
    mcmaster.append(position)
    #T
    position=draw(-258,200)
    mcmaster.append(position)
    position=draw(-260,200)
    mcmaster.append(position)
    position=draw(-260,220)
    mcmaster.append(position)
    position=draw(-260,200)
    mcmaster.append(position)
    position=draw(-262,200)
    mcmaster.append(position)
    #E
    position=draw(-264,200)
    mcmaster.append(position)
    position=draw(-264,210)
    mcmaster.append(position)
    position=draw(-264,220)
    mcmaster.append(position)
    position=draw(-268,220)
    mcmaster.append(position)
    position=draw(-264,220)
    mcmaster.append(position)
    position=draw(-264,210)
    mcmaster.append(position)
    position=draw(-268,210)
    mcmaster.append(position)
    position=draw(-264,210)
    mcmaster.append(position)
    position=draw(-264,200)
    mcmaster.append(position)
    position=draw(-268,200)
    mcmaster.append(position)
    #R
    position=draw(-270,200)
    mcmaster.append(position)
    position=draw(-270,220)
    mcmaster.append(position)
    position=draw(-270,200)
    mcmaster.append(position)
    position=draw(-274,200)
    mcmaster.append(position)
    position=draw(-274,210)
    mcmaster.append(position)
    position=draw(-270,210)
    mcmaster.append(position)
    position=draw(-274,220)
    mcmaster.append(position)
    #2
    position=draw(-280,200)
    mcmaster.append(position)
    position=draw(-284,200)
    mcmaster.append(position)
    position=draw(-280,220)
    mcmaster.append(position)
    position=draw(-284,220)
    mcmaster.append(position)
    #0
    position=draw(-286,200)
    mcmaster.append(position)
    position=draw(-286,220)
    mcmaster.append(position)
    position=draw(-286,200)
    mcmaster.append(position)
    position=draw(-290,200)
    mcmaster.append(position)
    position=draw(-290,220)
    mcmaster.append(position)
    position=draw(-286,220)
    mcmaster.append(position)
    position=draw(-290,220)
    mcmaster.append(position)
    #2
    position=draw(-292,200)
    mcmaster.append(position)
    position=draw(-296,200)
    mcmaster.append(position)
    position=draw(-292,220)
    mcmaster.append(position)
    position=draw(-296,220)
    mcmaster.append(position)
    #4
    position=draw(-298,200)
    mcmaster.append(position)
    position=draw(-298,210)
    mcmaster.append(position)
    position=draw(-302,210)
    mcmaster.append(position)
    position=draw(-302,200)
    mcmaster.append(position)
    position=draw(-302,220)
    mcmaster.append(position)

positions1=[]  #outer circle list of positions
positions2=[]  #inner circle list of positions
outer_border=[] #outer border list of positions
temp=[]  #temporary list of positions
temp1=[]  #temporary list of positions
temp2=[]  #temporary list of positions
temp3=[]   #temporary list of positions
mcmaster=[]  #list of McMaster 2024 list of positions
def main():    #All of the above functions are called in the main function in desired order
    turtle.bgcolor("black")
    t.speed(0)
    print("Please allow the program to finish the drawing, \n at some point you MAY NOT SEE IT working because of the lines overlapping, \n so PLEASE give it about 6 minutes to finish the drawing, However a message indicating that it is done will pop up")
    transition()
    outer_circle() 
    transition()
    inner_circle()
    transition()
    curved_lines(-215,-140,180,-185,-190,"normal")    #curved shape #1 from left
    transition()
    curved_lines(-185,-130,180,-150,-155,"normal")    #curved shape #2 from left
    transition()
    curved_lines(-147,-90,180,-110,-115,"normal")     #curved shape #3 from left
    transition()
    curved_lines(-105,-70,180,0,0,"reverse1")        #curved shape #4 from left
    transition()
    curved_lines(-70,-20,180,-40,-45,"normal")       #curved shape #5 from left
    transition()
    curved_lines(-365,-395,180,0,0,"side2")         #curved shape #6 from left
    transition()
    curved_lines(-365,-335,180,0,0,"side1")          #curved shape #7 from left
    transition()
    bottom_circle(-215,-335)                          #bottom semi circle
    transition()
    mcmaster_2024()                                   #MCMaster 2024 word
    transition()

    color_area(positions1,positions2,temp2,temp3)     #fills the background area within the shape with black color
    connect_dots(positions1)
    transition()
    connect_dots(positions2)
    t.left(156)         #This is to connect the two circles
    t.forward(20)
    transition()
    connect_dots(outer_border)
    transition()
    connect_dots(mcmaster)
    transition()
    t.hideturtle()
main()

x=input("\n Drawing finished. press any key to end the program")
if x=="y":
    SystemExit()

