from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = int(90)
DOWN = int(270)
LEFT = int(180)
RIGHT = int(0)

class Snake:
  def __init__(self):
    self.segments = []
    self.heading = RIGHT
    self.create_snake()

  def create_snake(self):
    for position in STARTING_POSITIONS:
      new_segment = Turtle(shape="square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    
    self.segments[0].setheading(self.heading)
    self.segments[0].forward(MOVE_DISTANCE)

  def up(self):
    if self.heading != DOWN:
      self.heading = UP

  def down(self):
    if self.heading != UP:
      self.heading = DOWN

  def left(self):
    if self.heading != RIGHT:
      self.heading = LEFT

  def right(self):
    if self.heading != LEFT:
      self.heading = RIGHT
