from turtle import Turtle, Screen, colormode
import random
my_turtle = Turtle()
my_turtle.shape("turtle")

my_screen = Screen()
colormode(255)

def change_color(q_turtle):
  c1 = random.randint(0, 255)
  c2 = random.randint(0, 255)
  c3 = random.randint(0, 255)
  q_turtle.pencolor((c1, c2, c3))

# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)

# # my_screen.exitonclick()

# for sides in range(3, 11):
#   colormode(255)
#   c1 = random.randint(0, 255)
#   c2 = random.randint(0, 255)
#   c3 = random.randint(0, 255)
#   my_turtle.color(c1, c2, c3)
#   for s in range(0, sides):
#     my_turtle.forward(100)
#     my_turtle.right(360 / sides)

# steps = 10
# my_turtle.pensize(15)

# for _ in range(0, steps):
#   change_color(my_turtle)
#   my_turtle.setheading(random.randint(0, 3) * 90)
#   my_turtle.forward(50)
  

# my_turtle.pensize(10)
# my_turtle.speed('fastest')
# gap_size = 15.0

# for n in range(int(360.0 / gap_size)):
#   my_turtle.circle(100)
#   my_turtle.setheading(my_turtle.heading() + gap_size)

import colorgram 

rgb_colors = []
colors = colorgram.extract('Day18-HirstPainting/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

matrix_size = 10
my_turtle.speed("fastest")
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
turn = True
for _ in range(matrix_size):
  for _ in range(matrix_size):
    my_turtle.dot(15, random.choice(rgb_colors))
    my_turtle.forward(50)

  my_turtle.backward(50)
  my_turtle.setheading(90)
  my_turtle.forward(50)
  if turn:
    my_turtle.setheading(180)
  else:
    my_turtle.setheading(0)
  turn = not turn

my_screen.exitonclick()