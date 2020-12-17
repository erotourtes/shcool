import random

def createShips():
    global ships
    eShips = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    length = sum(eShips)
    preLenght = 0
    while True:
        horizontal = random.randrange(1, 3)

        posX = 0
        posY = 0
        
        notReady = True
        for el in eShips:
            while notReady:
                posX = random.randrange(0, 10)
                posY = random.randomrange(0, (11 - el))


                for i in range(el):
                    ships[posX + i][posY] = 1
                    
                notReady = False

    print(ships)

    
ships = [[0 for i in range(10)] for i in range(10)]

createShips()
