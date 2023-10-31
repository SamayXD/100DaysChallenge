line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")
print("\nHiding your treasure! X marks the spot.")
position = input()
position = position.upper()


"""
if position == "A1":
    map[0][0] = "X"
elif position == "B1":
    map[0][1] = "X"
elif position == "C1":
    map[0][2] = "X"
elif position == "A2":
    map[1][0] = "X"
elif position == "B2":
    map[1][1] = "X"
elif position == "C2":
    map[1][2] = "X"
elif position == "A3":
    map[2][0] = "X"
elif position == "B3":
    map[2][1] = "X"
elif position == "C3":
    map[2][2] = "X"
else:
    print("You entered wrong location...")
"""

letter = position[0].upper() # if input: B2 => then letter is B (0 position of input)
abc = ["A", "B", "C"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1 # if input: B2 => then letter is 2 (1 position of input)

map[number_index][letter_index] = "X"
    
print("Your map is ready:")
print(f"{line1}\n{line2}\n{line3}")
