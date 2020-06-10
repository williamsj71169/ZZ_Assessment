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


def as_statement(statement, char):
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
# num2 = random.randint(lowest, highest)
# num3 = random.randint(lowest, highest)
# num4 = random.randint(lowest, highest)
# num5 = random.randint(lowest, highest)
# num6 = random.randint(lowest, highest)
# num7 = random.randint(lowest, highest)
# num8 = random.randint(lowest, highest)


print(num)
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# print(num5)
# print(num6)
# print(num7)
# print(num8)


# checks yes/no is really yes/no
def yn_checker():
    error = "Please choose yes or no (y / n) "
    valid = False
    while not valid:
        response = input("Would you like to see the instructions? ").lower()
        print()
        if response == "yes" or response == "y":
            return "Yes"
        elif response == "no" or response == "n":
            return "No"
        else:
            print(error)
            print()


yes_no = yn_checker()
if yes_no == "Yes":

    # instructions and welcome

    as_instructions = as_statement("--- Assessment - Instructions ---", "-")
    print("Welcome!")
    print("hi")
    print()
    print("----------------------------------------------")


# play_again loop start
play_again = ""
while play_again == "":

    rounds = intcheck("How many rounds?", 1, 10)
    print()

    rounds_played = 0

    while rounds_played < rounds:
        # output amount of rounds and guesses allowed
        print("Round {} of {}".format(rounds_played + 1, rounds))
        print()

        rounds_played += 1

        num = random.randint(lowest, highest)
        num1 = random.randint(lowest, highest)

        math = num + num1

        # rounds = intcheck("How many rounds?", 1, 10)  #
        question1 = intcheck("{} + {}".format(num, num1), math, math)
        if question1 == math:
            print("Well done!")
        elif question1 != math:
            print("Sorry, You Answer was Wrong!")
            print("Teh Answer was {}".format(math))

    print("You have gotten to the end of the game")

    play_again = (input("Push <enter> to play again/continue or any other key to quit"))

print("Thank You For Playing")
