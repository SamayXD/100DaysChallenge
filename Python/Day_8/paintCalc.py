import math

def checkPaint(wallHeight, wallWidth, coverage):
    canNums = (wallHeight*wallWidth)/coverage
    canNums = math.ceil(canNums)
    return canNums
    
wallHeight = int(input())
wallWidth = int(input())
coverage = 5

finalOut = checkPaint(wallHeight, wallWidth, coverage)

print(f"Total cans needed are {finalOut}")