import turtle
import math

bob=turtle.Turtle()
#tell the turtle what to do
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(80)
bob.left(90)
bob.forward(80)
bob.left(90)
bob.forward(60)


screen=turtle.getscreen()
screen.mainloop()


# functions/methods
# math function
# f(x) -> y
# input -> box -> output
# methods
# input -> box

def printHellos(name, name2):
	'''
	Prints hello to two people.
	'''
	
	print("Hello, " + str(name))
	print("Hello, " + str(name2))


def sqrt(n):
	if n<0:
		raise ValueError("The value must be non-negative")
	print(math.sqrt())
printHellos("bob",7)
sqrt(100)



