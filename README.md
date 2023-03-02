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

## Create snake's body
** To create body of the snake, you have to create a Snake class**
We change the default shape from turtle module to square: `var = Turtle(shape="square")` and make it white

## Make the snake move automatically
Create a `move` method. In this method, we have to use this principle to set up our entire snake movement:
> Every part of snake body have to follow the path of its previous part.

For example: The snake have 3 parts of body in the first place. When the snake's moving, the 3rd part have follow the 2nd part's previous path and the 2nd part follow the 1st part's previous path as well. That's mean only the first part(head) of the snake decide where the snake should go next

This is the code implementation of that principle:
```python
def move(self):
    for seq_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seq_num -1].xcor()
        new_y = self.seqments[seq_num -1].ycor()
        self.segments[seq_num].goto(new_x, new_y)
    self.segments[0].forward(20) #20 is the moving distance
```
### One important note when make the snake move is that:
We have to use `screen.tracer(0)` to disable all the animation on the screen and use `screen.update` to enable it back.
The reason is: We don't want to see the snake move part by part, we only want to see the image that every part have done moving. So combining all the image together, we have the snak move very smoothly

# Control the snake to turn up, down, right, left
Simply create 4 methods in the `snake.py` module
And in the `main.py`, we use `screen.listen()` to listen all the events that we make (pressing keyboard). Then we create four event-setup-key for each behavior (up, down, right, left) using `screen.onkey(FUNC, KEY)`

# The end---
