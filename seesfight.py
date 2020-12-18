from tkinter import *
from tkinter import messagebox
import time
import random

def createCircle():
    global positionX, positionY, counter, endgame, l1
    global firedShips, sumFiredShips
    prePositionX = -2
    prePositionY = -2
    if (positionX != prePositionX)  and (positionY != prePositionY) and (prePositionX != -1):
        if (ships[positionX][positionY] == 1) and (firedShips[positionX][positionY] != 1):
            canvas.create_oval(positionX * 50, positionY * 50, positionX *50 + 50, positionY * 50 +50,
                               fill = "red")
            counter = 0
            firedShips[positionX][positionY] = 1
            sumFiredShips +=1
        else:
            canvas.create_oval(positionX * 50, positionY * 50, positionX *50 + 50, positionY * 50 +50,
                               fill = "grey")
            if positionX != -1 and positionY != -1:
                counter += 1
    if counter > 5:
        endgame = True
        l1.place(x = 200, y = 200)
    
    prePositionX = positionX
    prePositionY = positionY

def onClose():
    global endgame
    if messagebox.askokcancel("EXIT", "Do U really wanna GIVE UP?"):
        endgame = True
        root.destroy()
        
def drawLines():
    for i in range(0, 10):
        canvas.create_line(i * 50, 0, i * 50, 600)
    for i in range(0, 10):
        canvas.create_line(0, i * 50, 600, i * 50)

def giveUP():
    global endgame, ships, l1, counter
    counter = 6
    endgame= True
    for i in range(10):
        for j in range(10):
            if ships[i][j] == 1:
                canvas.create_oval(i * 50, j * 50, i *50 + 50, j * 50 +50,
                               fill = "blue")
    for i in range(10):
        for j in range(10):
            if firedShips[i][j] == 1:
                canvas.create_oval(i * 50, j * 50, i *50 + 50, j * 50 +50,
                               fill = "red")
    l1.destroy()
    l1 = Label(root, text="U lose", width = 5, height = 2,  font = ("Arial", 50), bg = "red")
                

def refresh():
    global ships, canvas, counter, endgame, l1, firedShips, sumFiredShips, sumShips
    ships = [[0 for i in range(10)] for i in range(10)]
    firedShips = [[0 for i in range(10)] for i in range(10)]
    sumShips = 0
    createShips()
    sumFiredShips = 0
    canvas.delete("all")
    drawLines()
    counter = 0
    endgame = False
    l1.destroy()
    l1 = Label(root, text="U lose", width = 5, height = 2,  font = ("Arial", 50), bg = "red")
    

#check mouse position
def checkMouse(event):
    global positionX
    global positionY
    _type = 0
    if event.num == 3:
        _type = 1 #right click
    mouseX = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouseY = canvas.winfo_pointery() - canvas.winfo_rooty()
    positionX = mouseX // 50
    positionY = mouseY // 50
    if positionX < 0 or positionX > 9:
        positionX = -1
        positionY = -1
    if positionY < 0 or positionY > 9:
        positionY = -1
        positionX = -1
    if counter <= 5:
        createCircle()

def createShips():
    global ships, sumShips
    eShips = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    eShips.reverse()
    
    for el in eShips:
        horizontal = random.randint(0, 1)

        if horizontal == 0:
            posX = 0
            posY = 0
        
            notReady = True
            while notReady:
                posX = random.randint(0, 9)
                posY = random.randint(0, (10 - el))

                check = []

                for i in range(posX - 1, posX + 2):
                    for j in range(posY - 1, posY + el + 1):
                        try:
                            check.append(ships[j][i])
                        except:
                            pass

                check = set(check)
                if len(check) == 1:
                    notReady = False
                    for i in range(el):
                        ships[posY + i][posX] = 1
                        sumShips += 1
                        

        elif horizontal == 1:
            posX = 0
            posY = 0
        
            notReady = True
            while notReady:
                posX = random.randint(0, (10 - el))
                posY = random.randint(0, 9)

                check = []

                for i in range(posY - 1, posY + 2):
                    for j in range(posX - 1, posX + el + 1):
                        try:
                            check.append(ships[i][j])
                        except:
                            pass

                check = set(check)
                if len(check) == 1:
                    notReady = False
                    for i in range(el):
                        ships[posY][posX + i] = 1
                        sumShips+=1


endgame = False
positionX = -1
positionY = -1
#START PROGRAM
root = Tk()
root.geometry("700x600")
root.title("Fight")
root.resizable(False, False)
root.wm_attributes("-topmost", 1)
root.protocol("WM_DELETE_WINDOW", onClose)

canSize = 500

canvas = Canvas(root, width = canSize, height = canSize, bg = "white")
canvas.create_rectangle(0, 0, canSize, canSize, fill ="white")
canvas.place(x = 50, y = 50)

bFrame = Frame()
bFrame.place(x = 570, y = 50)

b0 = Button(bFrame, text ="Resign", width = 10, height = 10, font = ("Arial", 15), command = giveUP)
b1 = Button(bFrame, text = "Refresh", width = 10, height = 10, font = ("Arial", 15), command = refresh)
b0.pack()
b1.pack()

root.update()

canvas.bind_all("<Button-1>", checkMouse)
canvas.bind_all("<Button-3>", checkMouse)

drawLines()
#print q-p
text = "Q W E R T Y U I O P".split()
for i in range(10):
    Label(root, text = text[i], font = ("Arial", 15)).place(x = 65 + 50*i, y = 10)
#print from 1-10
#END SETTING UP FORM
for i in range(10):
    Label(root, text = str(i), font = ("Arial", 15)).place(x = 15, y = 60 + 50 * i)    


counter = 0
sumShips = 0
sumFiredShips = 0

#SET UP SHIPS
ships = [[0 for i in range(10)] for i in range(10)]
firedShips = [[0 for i in range(10)] for i in range(10)]
createShips()



l1 = Label(root, text="U lose", width = 5, height = 2,  font = ("Arial", 50), bg = "red")
while not endgame:
    if sumShips == sumFiredShips:
        print("WIN")
    #print(counter)
    print(sumShips, sumFiredShips)
    root.update()
    time.sleep(0.001)

