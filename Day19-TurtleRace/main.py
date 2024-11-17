from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?(red/green/blue): ").lower()

colors = ["red", "green", "blue"]
turtles = []
positions = [-150, 0, 150]
winner = ""
for index in range(0, 3):
  newTurtle = Turtle(shape="turtle")
  newTurtle.color(colors[index])
  turtles.append(newTurtle)
  newTurtle.penup()
  newTurtle.goto(x=-200,y=positions[index])
if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in turtles:
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)
    if turtle.xcor() > 200:
      is_race_on = False
      winner = turtle.pencolor()
      if winner == user_bet:
        print(f"You've won, the {winner} turtle is the winner!")
      else:
        print(f"You've lost, the {winner} turtle was the winner.")

screen.exitonclick()

