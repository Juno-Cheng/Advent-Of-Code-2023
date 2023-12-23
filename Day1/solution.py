

checker = '1234567890'

def find_first(line):
    for char in (line):
        if char.isdigit():
            return char
        
def find_last(line):
    for char in reversed(line):
        if char.isdigit():
            return char
    

def solution_1(text):
    split_text = text.split('\n')
    count = 0
    for line in split_text: #For each line
        first, last = 0, 0
        first = find_first(line)
        last = find_last(line)
        count += int(first)*10+int(last)
    return str(count)



        



    


#=================================Main===================================
document_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


print("Solution 1: " + solution_1(document_text))