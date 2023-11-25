# import turtle

# timmy = turtle.Turtle()

# print(timmy)

# my_screen = turtle.Screen()

# print(my_screen.canvheight)

# timmy.shape("turtle")
# timmy.color("coral")

# timmy.left(45)
# for i in range(0,100):
#     timmy.forward(2)

# timmy.right(90)
# for i in range(0,100):
#     timmy.forward(2)
    
# timmy.right(135)
# for i in range(0,100):
#     timmy.forward(3)

# my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ["Name", "Age"]
table.add_row(["Samay", 19])
table.add_row(["Nirmayee", 19])
table.add_row(["Prahtam", 19])

table.add_column("Gender", ["Male", "Female", "Male"])

table.align = "l"
print(table)