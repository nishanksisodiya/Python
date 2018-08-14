# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
import turtle #Outside_In
wn = turtle.Screen()
wn.bgcolor("#101010")
wn.title("Turtle")
skk = turtle.Turtle()
skk.shape("circle")
skk.color("blue")

def sqrfunc(size):
	for i in range(100):
		skk.fd(size)
		skk.left(90)

sqrfunc(0)
