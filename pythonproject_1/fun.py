# import turtle package
import turtle

# creating a turtle object(pen)
pen =  turtle.Turtle()

# defining a method to draw curve
def curve():
    for i in range(200):
        # defining step by stepcurve motion
        pen.right(1)
        pen.forward(1)
# defining method to draw a full heart
def heart():
            # set the fill color to red
            pen.fillcolor('red')


            # start filling the color
            pen.begin_fill()

            # draw the left line
            pen.left(140)
            pen.forward(113)

            #  draw the left curve
            curve()
            pen.left(120)

            # draw the right curve
            curve()

            # draw the right line
            pen.forward(112)

            # ending the filling of the color
            pen.end_fill()
# defining method to write text
def txt():
    # move turtle to air
    pen.up()
    # move turtle to a given position
    pen.setpos (-68, 95)
    # move the turtle to the ground
    pen.down()
    # set the text color to lightgreen
    pen.color('lightgreen')

    # write the specified text in
    # specified font style and size
    pen.write("AKSAN" , font=("Verdana" , 12 , "bold"))

# draw a heart
heart()
# write a text
txt()
# to hide turtle
pen.ht

