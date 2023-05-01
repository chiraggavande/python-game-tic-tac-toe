import turtle
import string
t=turtle.Turtle()
s=turtle.Screen()
t.speed(10)
t.hideturtle()
mat =[[0,0,0],[0,0,0],[0,0,0]]
turn = 0
player1 = s.textinput("Player 1 = 'O' ","Enter Player 1 name")
player2 = s.textinput("Player 2 = 'X' ","Enter Player 2 name")
   


def gameover():
    if(mat[0][0]==mat[0][1]==mat[0][2]=='x' or mat[1][0]==mat[1][1]==mat[1][2]=='x' or mat[2][0]==mat[2][1]==mat[2][2]=='x'or mat[0][0]==mat[1][1]==mat[2][2]=='x' or mat[2][0]==mat[1][1]==mat[0][2]=='x'or mat[0][0]==mat[1][0]==mat[2][0]=='x'or mat[0][1]==mat[1][1]==mat[2][1]=='x'or mat[0][2]==mat[1][2]==mat[2][2]=='x'):
        turtle.clearscreen() 
        t.goto(0,100)
        t.write(f"{player2.upper()} WINS",align='center',font=('Arial',30,'bold'))
        #print("X WINS")
        return True
    if(mat[0][0]==mat[0][1]==mat[0][2]=='o' or mat[1][0]==mat[1][1]==mat[1][2]=='o' or mat[2][0]==mat[2][1]==mat[2][2]=='o'or mat[0][0]==mat[1][1]==mat[2][2]=='o' or mat[2][0]==mat[1][1]==mat[0][2]=='o' or mat[0][0]==mat[1][0]==mat[2][0]=='o'or mat[0][1]==mat[0][1]==mat[2][1]=='o' or mat[0][2]==mat[1][2]==mat[2][2]=='o'):
        turtle.clearscreen()
        t.goto(0,100)
        t.write(f"{player1.upper()} WINS",align='center',font=('Arial',30,'bold'))
        #print("O wins")
        return True
    else:
        if(turn < 9 ):
            return False
        else:
            turtle.clearscreen()
            t.goto(0,100)
            t.write("DRAW",align='center',font=('Arial',30,'bold'))
            return True
        #else:
            #return False

        return False
def check(x,y):
    if(x<150 and x>-150 and y>-150 and y<150):
        if(x<-50 and y>50):#1
            if(mat[0][0]!=0):
                return False
            else:
                draw(-100,100)
                if(tur%2==0):
                    mat[0][0]='o'
                    return True
                else:
                    mat[0][0]='x'
                    return True
        elif(x>-50 and x<50 and y>50):#2
            if(mat[0][1]!=0):
                return False
            else:
                draw(0,100)
                if(tur%2==0):
                    mat[0][1]='o'
                    return True
                else:
                    mat[0][1]='x'
                    return True
        elif( x>50 and y>50):#3
            if(mat[0][2]!=0):
                return False
            else:
                draw(100,100)
                if(tur%2==0):
                    mat[0][2]='o'
                    return True
                else:
                    mat[0][2]='x'
                    return True
        elif( x<-50 and y<50 and y>-50):#4
            if(mat[1][0]!=0):
                return False
            else:
                draw(-100,0)
                if(tur%2==0):
                    mat[1][0]='o'
                    return True
                else:
                    mat[1][0]='x'
                    return True
        elif( x>50 and y<50 and y>-50):#6
            if(mat[1][2]!=0):
                return False
            else:
                draw(100,0)
                if(tur%2==0):
                    mat[1][2]='o'
                    return True
                else:
                    mat[1][2]='x'
                    return True
        elif( x<-50 and y<-50 ):#7
            if(mat[2][0]!=0):
                return False
            else:
                draw(-100,-100)
                if(tur%2==0):
                    mat[2][0]='o'
                    return True
                else:
                    mat[2][0]='x'
                    return True
        elif( x<50 and x>-50 and y<-50 ):#8
            if(mat[2][1]!=0):
                return False
            else:
                draw(0,-100)
                if(tur%2==0):
                    mat[2][1]='o'
                    return True
                else:
                    mat[2][1]='x'
                    return True
        elif(x>50 and y<-50 ):#9
            if(mat[2][2]!=0):
                return False
            else:
                draw(100,-100)
                if(tur%2==0):
                    mat[2][2]='o'
                    return True
                else:
                    mat[2][2]='x'
                    return True
        else:
            if(mat[1][1]!=0):#5
                return False
            else:
                draw(0,0)
                if(tur%2==0):
                    mat[1][1]='o'
                    return True
                else:
                    mat[1][1]='x'
                    return True
    else:
        return False


def p(x,y):   
    s.onscreenclick(None)
    s.onscreenclick(t.goto(x,y))
    if (check(t.xcor(),t.ycor())):
        if(gameover()):
            #print("game over")
            t.goto(0,0)
            t.write("GAME OVER",align='center',font=('Arial',30,'bold'))
            return 0
    s.onscreenclick(None)
    s.onscreenclick(p)

    
def draw(x,y):
    global turn
    global tur
    tur=turn
    if(turn%2==0):
        t.pu()
        t.goto(x-27,y-45)
        t.pd()
        t.write("O",font=('Arial',60,'bold'))
        #t.circle(10)
        t.pu()
        turn=turn+1
    else:
        t.pu()
        t.goto(x-25,y-45)
        t.pd()
        t.write("X",font=('Arial',60,'bold'))
        t.pu()
        turn=turn+1

       

def grid():
    t.up()
    t.goto(0,200)
    t.down()
    t.write("TicTacToe",align='center',font=('Arial', 16, 'bold'))


    t.up()
    t.goto(-50,150)
    t.down()
    t.goto(-50,-150)
    t.up()
    t.goto(50,-150)
    t.down()
    t.goto(50,150)
    t.up()
    t.goto(150,50)
    t.down()
    t.goto(-150,50)
    t.up()
    t.goto(-150,-50)
    t.down()
    t.goto(150,-50)
    t.up()


def gmloop():
    grid()
    s.onscreenclick(p,add=True)
    
    
gmloop()

turtle.mainloop()