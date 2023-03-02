# CONTROL SNAKE TO MOVE AROUND
> This version of snake game only do a few simple things:
> 1. Setup game screen
> 2. Create a snake body
> 3. Make the snake move automatically
> 4. Control the snake to turn up, down, right, left

## Setup game screen:
**First we have to import Screen class from turtle module**
```python
from turtle import Screen
```
**Then set the screen's width and height and change the background to black** using `.setup` and `.bgcolor`
```python
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
```
"Oh, don't forget to add an escape to the game: `screen.exitonclick()` - This will ensure that the game closes after running all the code and you have clicked on the screen.

