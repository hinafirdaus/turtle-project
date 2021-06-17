from turtle import*

radius = 180
penup()
setposition(0, -radius)
setheading(0)
pendown()
circle(radius)
mouth_radius = radius*0.6
mouth_angle=70
penup()
setposition(0, -mouth_radius)
setheading(0)
pendown()
circle(mouth_radius, mouth_angle)
penup()
setposition(0,-mouth_radius)
setheading(0)
pendown()
circle(mouth_radius, -mouth_angle)
eye_x=50
eye_y =50
eye_size=60
penup()
setposition(eye_x,eye_y)
pendown()
dot(eye_size)
penup()
setposition(-eye_x, eye_y)
pendown()
dot(eye_size)
