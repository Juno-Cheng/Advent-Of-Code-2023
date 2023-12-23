import string
import random

mapping = {
        "blue": 14, "red": 12, "green": 13
    }

#=================================Part 1===================================
def clean_up(line):
    newLine = ""
    for i in range(len(line)):
        if (line[i] == ':') or (line[i] == ';') or (line[i] == ','):
            newLine += " "
        else:
            newLine += line[i]

    testList = newLine.split(" ")
    newList = []
    for ii in range(len(testList)):
        if testList[ii] != "":
            newList.append(testList[ii])
    return newList

def calculate_id(text):
    total = 0
    split_text = text.split('\n')
    for line in split_text:
        #Default Parameters
        id, index = 0, 2

        current = (clean_up(line)) #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        id = int(current[1]) 
        while True:
            
            #print("Value: "+ current[index] + "Color: " + current[index+1])
            #print(current)

            if (int(current[index]) > mapping[current[index+1]]):
                id = 0
            
            index += 2

            if index == len(current)-2:
                break
        total += id
    return total



#=================================Part 2===================================

    


#=================================Main===================================
input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

print(calculate_id(input))