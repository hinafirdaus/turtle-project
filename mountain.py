from turtle import*


fillcolor("brown")
begin_fill()
for j in range(3):
    for i in range(3):
        left(120)
        forward(200)
    penup()
    forward(200)
    pendown()
end_fill()
penup()
backward(200)
left(90)
forward(250)
left(90)
forward(250)
pendown()
bgcolor("cyan")
fillcolor("yellow")
begin_fill()
circle(50)
end_fill()
