def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(0, 6):
    go()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
