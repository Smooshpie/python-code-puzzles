#https://open.kattis.com/problems/sibice

from math import sqrt

def checkFits(matchsize, length, width):
    if (checkLength(matchsize, length) or checkWidth(matchsize, width) or checkDiagonal(matchsize, length, width)):
        print("DA")
    else:
        print("NE")

def checkLength(matchsize, length):
    return matchsize <= length

def checkWidth(matchsize, width):
    return matchsize <= width

def checkDiagonal(matchsize, length, width):
    diagonal = sqrt(pow(length, 2) + pow(width, 2))
    return float(matchsize) <= diagonal

userInput = input("Please provide the number of dropped matches (1 <= x <= 50) and the size of the matchbox (width and length between 1 and 100): ").replace(" ","")
matches,width,length = map(int, userInput.split(","))
for x in range(matches):
    matchsize = int(input("Match size between 1 and 1000: "))
    checkFits(matchsize, width, length)
    
