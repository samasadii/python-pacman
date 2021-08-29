import msvcrt
import os
from colorama import *
from time import sleep
from random import *
init()
exflag=0
score = 0
def map(name):
    global conx
    global cony
    global enemies
    global score
    global walls
    global stars
    global numWalls
    map=open(name+".txt","r")
    extraWalls=map.readlines()
    numWalls=int((extraWalls[1])[:-1])
    conSize=[int((extraWalls[0])[:2]),int((extraWalls[0])[3:5])]
    conx=conSize[0]
    cony=conSize[1]
    walls=[]
    c=""
    for i in range(2,numWalls+2):
        c=""
        h=""
        m=0
        for n in extraWalls[i]:
            if n!=" ":
                c+=n
                m+=1
            elif n==" ":
                h=(extraWalls[i])[m+1:-1]
                break
        walls+=[[int(c)+1,int(h)+1]]
    enemies=extraWalls[len(extraWalls)-1]
    enemies=int(enemies[:-1])
    map.close()
    os.system("mode con: cols="+str(conx+5)+" "+"lines="+str(cony+5))
    score = 0
    stars=[]

def highScore():
    global score
    global hscore
    sc=open("highscore.txt","r")
    hscore=sc.read()
    sc.close()
    hscore=int(hscore)
    if score>hscore:
        hscore=score
    sc=open("highscore.txt","w")
    sc.write(str(hscore))
    sc.close


def enemy():
    global enemiesList
    global enemies
    global cony
    global conx
    global encol
    enemiesList=[]
    color=[Fore.RED,Fore.GREEN,Fore.MAGENTA,Fore.CYAN]
    encol=[]
    i=0
    while i<enemies:
        xen=randint(5,conx-1)
        yen=randint(5,cony-1)
        col=choice(color)
        if [xen,yen] not in (enemiesList and wallList):
            print col +place(xen,yen) +chr(235)
            enemiesList+=[[xen,yen]]
            encol+=[col]
            i+=1


def place(x,y):
    #choose the location for printing!
    return "\033["+str(y)+";"+str(x)+"H"

def newGame():
    global wallList
    global du #downup
    global rl #rightleft
    global walls
    global numWalls
    global cony
    global conx
    global score
    rl=2
    du=2
    for i in range (2,conx+2):
        for j in range (2,cony+2):
            print Fore.WHITE+Back.RESET +place(i,j) +chr(249)
    wallList=[]
    i=1
    for j in range (1,cony+3):
        print Back.BLUE+place(i,j)+" "
        wallList+=[[i,j]]
    i=conx+2
    for j in range (1,cony+3):
        print Back.BLUE+place(i,j)+" "
        wallList+=[[i,j]]
    j=1
    for i in range (1,conx+3):
        print Back.BLUE+place(i,j)+" "
        wallList+=[[i,j]]
    j=cony+2
    for i in range (1,conx+3):
        print Back.BLUE+place(i,j)+" "
        wallList+=[[i,j]]
    for n in range(numWalls):
        print Back.BLUE+place(walls[n][0],walls[n][1])+" "
    wallList+=walls
    print Fore.YELLOW +Style.BRIGHT+Back.RESET+ place(rl,du) +"@"
    enemy()
    move()

def enemy_move():
    global enemiesList
    global wallList
    global enemies
    global stars
    global encol
    i=0
    while i<enemies:
        go=randint(1,4)
        if go==1 and (([enemiesList[i][0],enemiesList[i][1]-1] not in wallList)):  #up
            enemiesList[i][1]-=1
            print encol[i]  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]) +chr(235)
            if [enemiesList[i][0],enemiesList[i][1]+1] in stars:
                print Fore.CYAN  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]+1) +" "
            else:
                print Fore.WHITE  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]+1) +chr(249)
            i+=1
        elif go==2 and (([enemiesList[i][0]+1,enemiesList[i][1]] not in wallList)):  #right
            enemiesList[i][0]+=1
            print encol[i]  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]) +chr(235)
            if [enemiesList[i][0]-1,enemiesList[i][1]] in stars:
                print Fore.CYAN  + Back.RESET +place(enemiesList[i][0]-1,enemiesList[i][1]) +" "
            else:
                print Fore.WHITE  + Back.RESET +place(enemiesList[i][0]-1,enemiesList[i][1]) +chr(249)
            i+=1
        elif go==3 and (([enemiesList[i][0],enemiesList[i][1]+1] not in wallList)):  #down
            enemiesList[i][1]+=1
            print encol[i]  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]) +chr(235)
            if [enemiesList[i][0],enemiesList[i][1]-1] in stars:
                print Fore.CYAN  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]-1) +" "
            else:
                print Fore.WHITE  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]-1) +chr(249)
            i+1
        elif go==4 and (([enemiesList[i][0]-1,enemiesList[i][1]] not in wallList)):  #left
            enemiesList[i][0]-=1
            print encol[i]  + Back.RESET  + Back.RESET +place(enemiesList[i][0],enemiesList[i][1]) +chr(235)
            if [enemiesList[i][0]+1,enemiesList[i][1]] in stars:
                print Fore.CYAN  + Back.RESET +place(enemiesList[i][0]+1,enemiesList[i][1]) +" "
            else:
                print Fore.WHITE  + Back.RESET +place(enemiesList[i][0]+1,enemiesList[i][1]) +chr(249)
            i+=1

def move():
    global rl #rightleft-x
    global du #downup-y
    global wallList
    global score
    global stars
    global enemies
    way=" "
    while True:
        sleep(0.125)
        enemy_move()
        if msvcrt.kbhit():
            way=msvcrt.getch()
        if (way=="w" or way=="W" or ord(way)==72) and ([rl,du-1] not in wallList): #up
            du-=1
            print Fore.WHITE  + Back.RESET + place(rl,du+1) +" "
            print Fore.YELLOW  +Style.BRIGHT+ Back.RESET + place(rl,du) +"@"
            if [rl,du] not in stars:
                stars+=[[rl,du]]
                score+=1
                print place(35,1)+ Back.BLUE + "Score \""+str(score)+"\""
        elif (way=="s" or way=="S" or ord(way)==80) and ([rl,du+1] not in wallList): #down
            du+=1
            print Fore.WHITE  + Back.RESET + place(rl,du-1) +" "
            print Fore.YELLOW  +Style.BRIGHT+ Back.RESET  + Back.RESET + place(rl,du) +"@"
            if [rl,du] not in stars:
                stars+=[[rl,du]]
                score+=1
                print place(35,1)+ Back.BLUE + "Score \""+str(score)+"\""
        elif (way=="d" or way=="D" or ord(way)==77) and ([rl+1,du] not in wallList): #right
            rl+=1
            print Fore.WHITE + Back.RESET + place(rl-1,du) +" "
            print Fore.YELLOW +Style.BRIGHT+ Back.RESET + place(rl,du) +"@"
            if [rl,du] not in stars:
                stars+=[[rl,du]]
                score+=1
                print place(35,1)+ Back.BLUE + "Score \""+str(score)+"\""
        elif (way=="a" or way=="A" or ord(way)==75) and ([rl-1,du] not in wallList): #left
            rl-=1
            print Fore.WHITE  + Back.RESET + place(rl+1,du) +" "
            print Fore.YELLOW  +Style.BRIGHT+ Back.RESET + place(rl,du) +"@"
            if [rl,du] not in stars:
                stars+=[[rl,du]]
                score+=1
                print place(35,1)+ Back.BLUE + "Score \""+str(score)+"\""
        elif way=="p":
            i=1
            where=" "
            os.system("cls")
            while True:
                if msvcrt.kbhit():
                    where=msvcrt.getch()
                    if i<=1 and ord(where)==80: #Down
                        i+=1
                    if i>=2 and ord(where)==72: #Up
                        i-=1
                if i==1:
                    print Fore.BLACK+Style.DIM+Back.YELLOW+place(2,1)+"Resume"
                    print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,2)+"Quit"
                if i==2:
                    print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,1)+"Resume"
                    print Fore.BLACK+Style.DIM+Back.YELLOW+place(2,2)+"Quit"
                if i == 1 and where=="\r":
                    resumeMap()
                    print Fore.YELLOW +Style.BRIGHT+Back.RESET+ place(rl,du) +"@"
                    way=" "
                    break
                if i == 2 and where=="\r":
                    highScore()
                    print Back.RESET+" "
                    os.system("cls")
                    return
        if [rl,du] in enemiesList or score==1879:
            highScore()
            print Back.WHITE+" "
            os.system("cls")
            print Fore.CYAN+Style.BRIGHT+place(37,13)+"Game Over"
            print Fore.BLUE+Style.BRIGHT+place(36,15)+"Score : "+str(score)
            print Fore.MAGENTA+Style.BRIGHT+place(32,20)+"press \"enter\" to exit"
            while True:
                if msvcrt.getch()=="\r":
                    print Back.RESET+" "
                    os.system("cls")
                    return

def resumeMap():
    global du #downup
    global rl #rightleft
    global cony
    global conx
    global stars
    global wallList
    global score
    g=1
    h=1
    for g in range (2,conx+2):
        for h in range (2,cony+2):
            if [g,h] not in stars:
                print Fore.WHITE+Back.RESET +place(g,h) +chr(249)
    for m in wallList:
        print Back.BLUE+place(m[0],m[1])+" "
    print Fore.YELLOW +Style.BRIGHT+Back.RESET+ place(rl,du) +"@"
    print place(35,1)+ Back.BLUE + "Score \""+str(score)+"\""
    for n in stars:
        print Back.RESET+place(n[0],n[1])+" "


def menu():
    global exflag
    highScore()
    global hscore
    i=1
    where=" "
    os.system("cls")
    while True:
        if msvcrt.kbhit():
            where=msvcrt.getch()
            if i<=2 and ord(where)==80:
                i+=1
            if i>=2 and ord(where)==72:
                i-=1
        if i==1:
            print Fore.BLACK+Style.DIM+Back.YELLOW+place(2,1)+"New Game"
            print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,2)+"High Score"
            print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(1,3),"Quit"
        if i==2:
            print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,1)+"New Game"
            print Fore.BLACK+Style.DIM+Back.YELLOW+place(2,2)+"High Score"
            print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,3)+"Quit"
        if i==3:
            print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,1)+"New Game"
            print Fore.YELLOW+Style.BRIGHT+Back.RESET+place(2,2)+"High Score"
            print Fore.BLACK+Style.DIM+Back.YELLOW+place(2,3)+"Quit"
        if i==1 and where=="\r":
            os.system("cls")
            mname=raw_input(""" enter map's name
            """)
            map(mname)
            newGame()
            where=" "
            os.system("cls")
        if i==2 and where=="\r":
            highScore()
            os.system("cls")
            print Fore.YELLOW+Style.DIM+Back.RESET+place(13,3)+"High Score"
            print Fore.YELLOW+Style.DIM+Back.RESET+place(16,5)+str(hscore)
            print Fore.YELLOW+Style.DIM+Back.RESET+place(2,7)+"press \"enter\" to get back to menu"
            while True:
                if msvcrt.getch()=="\r":
                    where=" "
                    os.system("cls")
                    break
        if i==3 and where=="\r":
            exflag=1
            return

if exflag==0:
    menu()

os.system("exit")
