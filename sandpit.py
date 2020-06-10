import random


def intcheck(question, low, high):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                print("Well done")
                return response

            elif low >= response >= high:
                print("The answer is between 0 and 1000")

            else:
                print("WRONG!!")
                print()
        except ValueError:
            print("Please enter an integer")
            print()


lowest = 0
highest = 1000

play_again = ""
while play_again == "":

    num = random.randint(lowest, highest)
    num1 = random.randint(lowest, highest)

    math = num + num1

    # rounds = intcheck("How many rounds?", 1, 10)  #
    round1 = intcheck("{} + {}".format(num, num1), math, math)

    play_again = (input("Push <enter>"))

print("Thank You For Playing")