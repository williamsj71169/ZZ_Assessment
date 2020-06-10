import random


def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()


def hl_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""


lowest = 0
highest = 1000

num = random.randint(lowest, highest)
num1 = random.randint(lowest, highest)
num2 = random.randint(lowest, highest)
num3 = random.randint(lowest, highest)
num4 = random.randint(lowest, highest)
num5 = random.randint(lowest, highest)
num6 = random.randint(lowest, highest)
num7 = random.randint(lowest, highest)
num8 = random.randint(lowest, highest)


print(num)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
