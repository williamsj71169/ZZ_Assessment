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

# num3 = random.randint(lowest, highest)
# num4 = random.randint(lowest, highest)
# num5 = random.randint(lowest, highest)
# num6 = random.randint(lowest, highest)
# num7 = random.randint(lowest, highest)
# num8 = random.randint(lowest, highest)


# checks yes/no is really yes/no
def yn_checker(question):
    error = "Please choose yes or no (y / n) "
    valid = False
    while not valid:
        response = input(question).lower()
        print()
        if response == "yes" or response == "y":
            return "Yes"
        elif response == "no" or response == "n":
            return "No"
        else:
            print(error)
            print()


yes_no = yn_checker("Would you like to see the instructions? ")
if yes_no == "Yes":

    # instructions and welcome

    as_instructions = as_statement("--- Assessment - Instructions ---", "-")
    print("Welcome!")
    print("hi")
    print()
    print("---------------------------------")


# play_again loop start
play_again = ""
while play_again == "":

    # '''
    num = random.randint(lowest, highest)
    print(num)
    num1 = random.randint(lowest, highest)
    print(num1)

    two_three = intcheck("Would you like 2 numbers or 3?", 2, 3)
    if two_three == 2:
        question1 = ("{} + {} = ".format(num, num1))
        print("hhi")
    else:
        print("lol")
        question1 = intcheck("lol", 1, 4)
    # '''

    rounds = intcheck("How many rounds?", 1, 10)
    print()

    win = 0
    lose = 0
    rounds_played = 0

    while rounds_played < rounds:
        # output amount of rounds and guesses allowed
        round_of_rounds = as_statement("*** Round {} of {} ***".format(rounds_played + 1, rounds), "*")

        print()

        rounds_played += 1

        num = random.randint(lowest, highest)
        print(num)
        num1 = random.randint(lowest, highest)
        print(num1)

        math = num + num1
        result = "{} + {} : User: {}, Answer: {}".format(num, num1, question1, math)
        game_summary = []  # Holds results from each round

        # question1 = intcheck("{} + {}".format(num, num1), 0, 2000)
        print(intcheck(question1, 0, 2000))
        if question1 == math:
            print("Well done!")
            win += 1
        elif question1 != math:
            print()
            lose += 1
            print("Sorry, You Answer was Wrong!")
            print("The Answer was {}".format(math))

        game_summary.append("Round #{} = {}".format(rounds_played, result))

        print()
        print("You have gotten to the end of the game")
        # End of game, Print Stats
        print()
        print("**** Game History ****")
        for item in game_summary:
            print(item)

    final = as_statement("### Wins:{}  |  Losses:{} ###".format(win, lose), "#")

    play_again = (input("Push <enter> to play again/continue or any other key to quit"))
