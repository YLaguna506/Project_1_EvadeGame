# Laguna_96642_project01_EvadeGame
My first project game for my python class.

The primary objective of this game is to evade the enemy cubes. 
When you click the screen the game countdown starts. After 5 seconds the game starts.
If you collide with the screen borders, you lose,
If you collide with the enemy cubes, you lose.
After you lose, you decide if you want to play again or not.

The running score is how many cubes you have evaded.

If you survive long enough the game gets harder and harder.

To control the main cube, you must use the keyboard keys 'wasd'.
The enemy cubes at the start, begin to fall down until they reach the bottom. 
Then they will fall from the sky continuously at random y - axis ranges.
All of this is done thanks to infinite loops, and the time.sleep() function.
75 enemy cubes are created from the start.


I had to modify the graphics module and include 4 new functions to the Rectangle object.
The 4 new functions are 'getx_1', 'getx_2', 'gety_1' and 'gety_2'.
This functions return the x and y values of the 2 points of the rectangle.



main.py contains first prototype of the game. It was made with classes.

Evade_B contains the game but without the implementation of classes. It just uses functions.

Evade_C is the final version of the game. It contains classes and functions. 
I modified the moves of the cube into toggle. You have to keep pressing the keyboard button for the cube to move.
On the other versions, the cube moved on its own and you were just able to change the direction the cube goes in.
