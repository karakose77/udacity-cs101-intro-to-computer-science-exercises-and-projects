import turtle

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


def initialize(turtle_shape, bg_color, turtle_color, turtle_speed):
    """
    Initializes turtle instance for turtle game.
    """
    turtle_instance = turtle.Turtle()
    turtle_instance.shape(turtle_shape)
    turtle.bgcolor(bg_color)
    turtle_instance.color(turtle_color)
    turtle_instance.speed(turtle_speed)
    return turtle_instance


def turtle_movement(turtle_shape, bg_color, turtle_color, turtle_speed):
    """
    Defines the turtle movement for the initialized turtle instance
    and executes that movement.
    """
    turtle_name = initialize(turtle_shape, bg_color,
                             turtle_color, turtle_speed)

    for i in range(36):
        for i in range(4):
            turtle_name.forward(200)
            turtle_name.right(90)
        turtle_name.right(10)


turtle_movement("turtle", "orange", "purple", 8)
