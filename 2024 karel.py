from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
from karel.stanfordkarel import *

"""
File: 2024.py
--------------------
When you finish writing this file, Karel should be able to 
place 20 beepers, then 24 beepers, and end facing East to 
the right of the 24 beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # your code here
    
    while front_is_clear():
        for i in range(20): 
                put_beeper()
        move()
        for i in range(24): 
                put_beeper()
        move()

        

    
if __name__ == '__main__':
    main()
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
