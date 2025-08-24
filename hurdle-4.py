def turn_right():
    for i in range(3):
        turn_left()

def jump():
    for i in range(1 < 14):
        move()
    if right_is_clear():
        turn_right()

while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear():
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
# def turn_right():
#     for i in range(3):
#         turn_left()

# def moving():
#     for i in range(1 < 5):
#         move()
#     if right_is_clear():
#         turn_right()
        
# while not at_goal():
#     if wall_in_front():
#         turn_left()
#     elif front_is_clear():
#         moving()


# def turn_right():
#     for i in range(3):
#         turn_left()
 
# while not at_goal():
#     if front_is_clear():
#         move()
#     if wall_in_front() and wall_on_right():
#         turn_left()
#     if right_is_clear():
#         turn_right()
        