from tkinter import *
from tkinter import messagebox
import time
import random

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
    pass
def refresh():
    pass

def addToAll(event):
    _type = 0
    if event.num == 3:
        _type = 1 #right click
    mouseX = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouseY = canvas.winfo_pointery() - canvas.winfo_rooty()
    positionX = mouseX // 50
    positionY = mouseY // 50
    print(positionX, positionY)

def createShips():
    ships = [[0 for i in range(10)] for i in range(10)]
    eShips = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    length = sum(eShips)
    preLenght = 0
    while preLength != length:
        horizontal = random.randrange(1, 3)

        if horizontal == 0:
            fail = False
            generateX = random.randrange(1, 3)
            
    print(ships)
endgame = False

root = Tk()
root.geometry("700x600")
root.title("Fight")
root.resizable(False, False)
root.wm_attributes("-topmost", 1)
root.protocol("WM_DELETE_WINDOW", onClose)

canSize = 500

canvas = Canvas(root, width = canSize, height = canSize, bg = "white")
canvas.create_rectangle(0, 0, canSize, canSize, fill ="white")
canvas.pack(side = LEFT, padx=50)

bFrame = Frame()
bFrame.pack(side = LEFT)

b0 = Button(bFrame, text ="Give up", width = 10, height = 10, font = ("Arial", 15), command = giveUP)
b1 = Button(bFrame, text = "Refresh", width = 10, height = 10, font = ("Arial", 15), command = refresh)
b0.pack()
b1.pack()

root.update()

drawLines()
createShips()



canvas.bind_all("<Button-1>", addToAll)
canvas.bind_all("<Button-3>", addToAll)

while not endgame:
    root.update()
    time.sleep(0.001)
