

def extract_symbols(input_data):
    unique_symbols = set()
    numbers = "0123456789"
    for line in input_data.split("\n"):
        for char in line:
            if char not in numbers and char != '.' and char.isprintable():
                unique_symbols.add(char)
    return unique_symbols

print(extract_symbols(x))