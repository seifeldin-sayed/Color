from turtle import *
speed(10)
bgcolor("white")
penup()
goto(-50,-100)
pendown()
color("black")
begin_fill()
for i in range(6):
    forward(100)
    left(60)
end_fill()
penup()
goto(-42,-84)
pendown()
color("white")
begin_fill()
for i in range(6):
    forward(84)
    left(60)
end_fill()
penup()
goto(-40,-80)
pendown()
color("orange")
begin_fill()
for i in range(6):
    forward(80)
    left(60)
end_fill()
penup()
goto(0,15)
pendown()
color("black")
begin_fill()
goto(15,15)
left(75)
forward(30)
goto(50,-10)
goto(25,-30)
goto(10,-70)
goto(0,-70)
end_fill()
penup()
goto(0,15)
pendown()
color("black")
begin_fill()
goto(-15,15)
left(30)
forward(30)
goto(-50,-10)
goto(-25,-30)
goto(-10,-70)
goto(0,-70)
end_fill()
penup()
goto(5,-20)
pendown()
color("white")
begin_fill()
goto(15,-20)
goto(15,-10)
goto(5,-20)
end_fill()
penup()
goto(-5,-20)
pendown()
color("white")
begin_fill()
goto(-15,-20)
goto(-15,-10)
goto(-5,-20)
end_fill()
penup()
goto(0,-400)
pendown()
done()