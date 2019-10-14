import turtle

def draw_square(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
        
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("red")

lorenzo = turtle.Turtle()
lorenzo.shape("turtle")
lorenzo.color("blue")

draw_square(bob, 100)
draw_square(lorenzo, 50)
        
