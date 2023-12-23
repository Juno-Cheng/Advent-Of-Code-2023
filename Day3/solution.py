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

def calculateList(list):
    value = 0
    index = len(list) - 1
    for item in list:
        tens = 1
        for i in range(index):
            tens = tens * 10
        value += int(item) * tens
        index -= 1
    return value

def findSymbol(list ,col, row, length): #Finds symbol in an area
    #Symbols
    symbol = "$#*"
    #Checks neighbors
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if (col + x) < 0 or (col + x) > length or (row + y) < 0 or (row + y) > length:
                continue
            elif (list[col+x][row+y] in symbol):
                return True
    return False
#=================================Part 1===================================
checker = "1234567890"
def solution_1(input):
    matrix = TwoDList(input)
    total = 0


    row = 0
    for line in matrix:
        values = [] #Get values in a line
        positions = []#Get starting location of each value
        index = 0
        print(line)
        num = []
        for item in line:

            if num == [] and ((item) in checker): #Number is found, num is empty, add and add index
                print("Condition 1\n")
                num.append((item))
                positions.append(index)
            elif num != [] and ((item) in checker): #Number is found, num is not empty, simply add
                print("Condition 2\n")

                num.append((item))

            elif num == [] and  ((item) not in checker): #Symbol/. is found, but num is empty, continue
                print("Condition 3\n")
                continue

            elif num != [] and  ((item) not in checker): #Symbol/. is found, but num is not empty, continue
                print("Condition 4\n")

                values.append(calculateList(num))
                num = []
            index += 1
        
        print(values)
        print(positions)
        #Check if values/position are valid
        for i in range(len(values)-1):
            if findSymbol(matrix, positions[i], row, len(str(values[i]))) == True:
                total += int(values[i])
        row += 1

        return total






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

print(solution_1(input))


