
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

two_three = intcheck("Would you like 2 numbers or 3?", 2, 3)
if two_three == 2:
    print("hhi")
else:
    print("lol")
