"""
names = ['qq', 'ww', 'ee']

for items in names:
    if items == "ww":
        indexx = names.index(items)
        print(f"---> {items} at {indexx+1}")
    else:
        print(items)
"""

#===========================================>
totalEven = 0
totalOdd = 0
for i in range(1, 101):
    if i%2 == 0:
        totalEven += i
    else:
        totalOdd +=i

print(f"Total of all EVEN between 1 to 100 is {totalEven}")
print(f"Total of all ODD between 1 to 100 is {totalOdd}")
print(f"Total of all nums between 1 to 100 is {totalEven + totalOdd}")
#===========================================>


