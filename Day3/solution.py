import string
import random



#=================================Part 1===================================
symbols = {'/', '$', '#', '@', '*', '&', '-', '=', '+', '%'}
numbers = "0123456789"

def check_adjacent(matrix, row, start_col, length, max_rows, max_cols):
    values = [-1, 0, 1]
    for i in range(length):  # Iterate over each digit in the number
        col = start_col - length + i  # Calculate the column position for each digit
        for x in values:
            for y in values:
                if x == 0 and y == 0:
                    continue  # Skip the number itself

                adj_row = row + x
                adj_col = col + y

                if 0 <= adj_row < max_rows and 0 <= adj_col < max_cols:
                    if matrix[adj_row][adj_col] in symbols:  # Ensure 'symbols' is defined
                        return True
    return False

def Matrix(input):
    lines = input.split('\n')
    matrix = [list(line) for line in lines]
    return matrix

def solution_1(input):
    matrix = Matrix(input)
    total_sum = 0
    max_rows = len(matrix)
    max_cols = len(matrix[0]) if max_rows > 0 else 0

    for row, line in enumerate(matrix):
        number = ""
        column = 0
        while column < len(line):
            char = line[column]
            if char.isdigit():
                number += str(char)
            else:
                if number:
                    # Check if the number is adjacent to a symbol
                    if check_adjacent(matrix, row, column, len(number), max_rows, max_cols):
                        total_sum += int(number)
                number = ""
            column += 1  # Increment column index

        if number:
            if check_adjacent(matrix, row, column, len(number), max_rows, max_cols):
                print(number)
                total_sum += int(number)

    return total_sum


#=================================Part 2===================================







#=================================Main===================================
input = """"""

print(solution_1(input))


