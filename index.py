import sys

def add(numbers):
    if not numbers:
        return 0
    
    seperated_numbers = [int(i) for i in numbers.split(',')]

    return sum(seperated_numbers)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            result = add(i)
            print(f"input = {i}, output = {result}")
    else:
        print("Please add a string arg to calculate")