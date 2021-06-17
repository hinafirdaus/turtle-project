from turtle import *
while True: 
    side = int(input("Enter the length of sqaure sides: "))
    i=0
    for i in range(4):
        forward(side)
        right(90)
