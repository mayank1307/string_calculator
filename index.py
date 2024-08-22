import sys, re

def get_numbers_from_string(input_string):
    if input_string.startswith('//'):
        delimiter, numbers = input_string.split('\n',1)
        if not numbers:
            return []
        return re.split(re.escape(delimiter[2:]) + r'|\n', numbers)

    else:
        delimiter_pattern = ',|\n'
        return re.split(delimiter_pattern, input_string)

def add(numbers):
    if not numbers:
        return 0

    seperated_string = get_numbers_from_string(numbers)

    if not seperated_string or not len(seperated_string):
        return 0

    seperated_numbers = [int(i) for i in seperated_string]

    return sum(seperated_numbers)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            result = add(i)
            print(f"input = {i}, output = {result}")
    else:
        print("Please add a string arg to calculate")