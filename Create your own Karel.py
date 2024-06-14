from karel.stanfordkarel import *

# Comments can be included in any part of a program. 
# They start with a # and include the rest of the line.
# The computer will ignore them, but they are very helpful for human readers!

def main():
    # example program to move, put_beeper, move
    move()
    put_beeper()
    move()

# Function Declaration

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Conditions Example

def safe_move():
    if front_is_clear():
        move()

# For Loop Example

def place_100_beepers():
    for i in range(100):
        put_beeper()

# While Loop Example

def move_to_wall():
    while front_is_clear():
        move()

# Karel Conditions

# front_is_clear()
# beepers_present()
# beepers_in_bag()
# left_is_clear()
# right_is_clear()
# facing_north()
# facing_south()
# facing_east()
# facing_west()

# Opposite Conditions
# front_is_blocked()
# no_beepers_present()
# no_beepers_in_bag()
# left_is_blocked()
# right_is_blocked()
# not_facing_north()
# not_facing_south()
# not_facing_east()
# not_facing_west()

# Additional Commands Example

def advanced_commands_example():
    # this will pass 80% of the time
    if random(0.8):
        # create a blue square
        paint_corner("blue")
    # checks if the current square is blue
    if corner_color_is("blue"):
        move()

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()
