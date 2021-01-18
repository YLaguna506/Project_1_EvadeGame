from graphics_yael import *
import time
import random

# --- classes ---

#class of cube player controlls
class Player:
    def __init__(self, window, character):
        self.p1 = character
        self.win = window

        self.p1.setFill(color_rgb(0, 255, 0))
        self.p1.draw(self.win)

    def movement(self):
        if self.win.lastKey == "d":
            self.p1.move(20, 0)
        if self.win.lastKey == "a":
            self.p1.move(-20, 0)
        if self.win.lastKey == "s":
            self.p1.move(0, 10)
        if self.win.lastKey == "w":
            self.p1.move(0, -10)


#class of Enemy AI cubes
class Enemy:
    def __init__(self, window, rect, color):
        self.win = window
        self.rect = rect
        self.color = color

        self.rect.setFill(self.color)
        self.rect.draw(self.win)

    def movement(self):
        dx = 0
        dy = 9
        self.rect.move(dx, dy)


    # Return new Rectangle whose points are its lower-left and upper-right
    #    extrema.
def canonical_rect(rect):

    p1, p2 = rect.p1, rect.p2

    min_x = min(p1.x, p2.x)
    min_y = min(p1.y, p2.y)

    max_x = max(p1.x, p2.x)
    max_y = max(p1.y, p2.y)

    return Rectangle(Point(min_x, min_y), Point(max_x, max_y))


#  Determine whether the two arbitrary Rectangles intersect.
def intersect(rect1, rect2):

    r1, r2 = canonical_rect(rect1), canonical_rect(rect2)

    return (r1.p1.x <= r2.p2.x and r1.p2.x >= r2.p1.x and
            r1.p1.y <= r2.p2.y and r1.p2.y >= r2.p1.y)

# --- Main ---


# Initial points for cube player controlls
point1 = Point(350, 210)
point2 = Point(380, 240)

# Initial points for AI cubes
point3 = Point(10, 30)
point4 = Point(30, 10)

win = GraphWin("mini graphic game", 800, 500)

# Creates starting window
win.setBackground("green")
title = Text(Point(400, 150), "EVADE GAME")
title2 = Text(Point(400, 200), "Created by Yael Laguna")
title3 = Text(Point(400, 350), "Click screen to start game")
title.setTextColor("black")
title2.setTextColor("black")
title3.setTextColor("black")
title.setSize(20)
title2.setSize(20)
title3.setSize(20)
title.draw(win)
title2.draw(win)
title3.draw(win)

win.getMouse()

i = 0 # used for undrawing title4 after one session


# while the player wants to keep playing
repeat = True
while repeat:

    title.undraw()
    title2.undraw()
    title3.undraw()
    if i > 0:
        title4.undraw()

    win.setBackground("black")

    # Creation of player and enemy cubes
    p1 = Player(win, Rectangle(point1, point2))
    AI = [Enemy(win, Rectangle(point3, point4), "blue") for _ in range(75)]

    num_evaded = -75 # score, after start of the game value turns into 0

    countdown = 5 # Countdown timer for game to begin
    y = 0 # used for displaying countdown properly
    s = 0 # used for displaying 'Game Starts' properly
    start = False

    while not win.isClosed():

        collision = False

        p1.movement()

        # This part is the 5 second countdown initial part of the game
        # The Enemy cubes are moving themselves until they start falling from the sky
        n = 0
        while not win.isClosed():
            if n >= 75:
                break
            x = 1
            if not start:
                if y % 75 == 0:
                    print("Countdown to Start: ", countdown, "!")
                    countdown -= 1
                y += 1

                while x <= 10:
                    AI[n].movement()
                    x += 1

            AI[n].movement()
            n += 1

        # Check if main cube collides with walls on x - axis.
        if p1.p1.getx_2() >= 800 or p1.p1.getx_1() <= 0:
            print("Hit Wall on X - axis!")
            break

        # Checks if main cube collides with walls on x - axis.
        elif p1.p1.gety_2() >= 500 or p1.p1.gety_1() <= 0:
            print("Hit Wall on Y - axis!")
            break

        # Checks for intersection of enemy cubes with main cube
        n = 0
        while n < 75:

            if intersect(p1.p1, AI[n].rect):
                print("Collision")
                collision = True
            n += 1

        if collision == True:
            break

        # Makes enemy cubes fall from the sky after hitting ground continuously
        n = 0
        while n < 75:

            if AI[n].rect.gety_2() >= 500:
                num_evaded += 1
                AI[n].rect.move((AI[n].rect.getx_1() * -1), (AI[n].rect.gety_1() * -1) + random.randint(-1000, 0))
                AI[n].rect.move(random.randint(0, 800), 0)

                start = True

            if start and s == 0:
                print("GAME STARTS!")
                print("TRY TO SURVIVE!")
                s += 1

            n += 1

        # Value used for speed of the game
        sleep_value = 0.10

        # Prints score of enemy cubes evaded
        if num_evaded > 0:
            print("Cubes evaded: ", num_evaded)

        # Increses speed and difficulty of the game after evading 250 enemy cubes
        if num_evaded >= 250:
            sleep_value = 0.05

        # Increses speed and difficulty of the game after evading 500 enemy cubes
        if num_evaded >= 500:
            sleep_value = 0.03

        # Increses speed and difficulty of the game after evading 1000 enemy cubes
        if num_evaded >= 1000:
            sleep_value = 0.01

        win.update()
        time.sleep(sleep_value)

    # Showcases interface after losing a session of the game
    win.setBackground("red")
    title = Text(Point(400, 150), "EVADE GAME")
    title2 = Text(Point(400, 200), "Created by Yael Laguna")
    title3 = Text(Point(400, 300), "End of game")
    title4 = Text(Point(400, 350), "Click left side of screen to start again, or click right side of screen to quit")
    title.setTextColor("black")
    title2.setTextColor("black")
    title3.setTextColor("black")
    title4.setTextColor("black")
    title.setSize(20)
    title2.setSize(20)
    title3.setSize(20)
    title4.setSize(18)
    title.draw(win)
    title2.draw(win)
    title3.draw(win)
    title4.draw(win)

    # Checks if player clicks left side of the screen to play again
    value = win.getMouse()
    if value.getX() <= 399:
        #print("YES")
        repeat = True
        i += 1

    # Checks if player clicks right side of the screen to quit the game
    elif value.getX() > 399:
        #print("NO")
        repeat = False

    # Undraws all cubes
    p1.p1.undraw()
    n = 0
    while n < 75:
        AI[n].rect.undraw()
        n += 1

win.close()
