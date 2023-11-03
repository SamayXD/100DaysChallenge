"""
Solution for : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

a simple hurdle question
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
num_hurd = 6
   
for i in range(0,num_hurd):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
