import string
import random



#=================================Aux===================================

def TwoDList(input): #Turns String to 2D Matrix
    split_text = input.split('\n')#Gets each line
    main = []
    for line in split_text:
        sub = []
        for char in line:
            sub.append(char)
        main.append(sub)

    return main


def findSymbol(col,row): #Finds symbol in an area
    #Symbols
    symbol = "$#*"
    #Checks neighbors
    if (row != 0):
        if 
#=================================Part 1===================================

    





#=================================Part 2===================================

    





#=================================Main===================================
input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

print(TwoDList(input))