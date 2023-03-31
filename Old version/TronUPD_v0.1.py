from turtle import *
import random
from freegames import *


print("Please enter nicknames")
nickP1 = input("First nickname for blue player: ")
nickP2 = input("Second nickname for orange player: ")

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    """Return True if head inside screen."""
    return -380 < head.x < 380 and -380 < head.y < 380

def mine():
    global minesCoords
    coordsX = []
    coordsY = []
    minesCoords = []
    for i in range(30):
        x = random.randint(-420, 420)
        y = random.randint(-420, 420)
        coordsX.append(x)
        coordsY.append(y)
        square(x, y, 10, 'red')
        update()
    minesCoords.append(coordsX)
    minesCoords.append(coordsY)
    print(minesCoords)

def minesHitBox():
        for i in range(30):
            if ((p2head[0] <= minesCoords[0][i]+6 and p2head[0] >= minesCoords[0][i]-6) and (p2head[1] <= minesCoords[1][i]+6 and p2head[1] >= minesCoords[1][i]-6)):
                print(f"Mine detected! Player {nickP1} lost!")
                quit()
        
        for i in range(30):
            if ((p1head[0] <= minesCoords[0][i]+6 and p1head[0] >= minesCoords[0][i]-6) and (p1head[1] <= minesCoords[1][i]+6 and p1head[1] >= minesCoords[1][i]-6)):
                print(f"Mine detected! Player {nickP2} lost!")
                quit()
            
def draw():
    """Advance players and draw game."""
    global p1head, p2head
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body or p1head in p1body:
        print(f'Player {nickP1} wins!')
        print(f'Player cords: {p1head}')
        return  

    if not inside(p2head) or p2head in p1body or p2head in p2body:
        print(f'Player {nickP2} wins!')
        print(f'Player cords: {p2head}')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'orange')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    minesHitBox()
    ontimer(draw, 50)


setup(600, 600, 500, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'Left')
onkey(lambda: p2aim.rotate(-90), 'Right')
mine()
draw()
done()