# imports a random number (used for both numbers)
import random

# checks that what you are inputting is an integer


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


# adds 'decoration' to outputs. Adds characters above and below statement so that statement stands out
def as_statement(statement, char):
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""

# establishes the high and low for numbers in questions
lowest = 0
highest = 1000


# checks that inputted yes/no is really yes/no
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

# asks user if they would like to see the instructions
yes_no = yn_checker("Would you like to see the instructions? ")
if yes_no == "Yes":

    # instructions and welcome
    as_instructions = as_statement("--- Assessment - Instructions ---", "-")
    print("Welcome!")
    print("This Game is easy, answer the ")
    print("maths questions!!")
    print("At the start of a new 'game' you can choose ")
    print("to continue with your previous scores or ")
    print("start anew.")
    print()
    print("---------------------------------")

win = 0
lose = 0
games_played = 0

end = []  # Holds results from each round

# play_again loop start
play_again = ""
while play_again == "":

    # asking the player if they would like to re-start their score
    games_played += 1
    if games_played > 1:
        print("")
        yes_no = yn_checker("Would you like to re-start your score board? ")
        if yes_no == "Yes":
            losses = 0
            wins = 0
            ties = 0
    print("Game {}".format(games_played))

    game_summary = []  # Holds results from each round

    print()
    # asks user how many round they would like to play
    rounds = intcheck("How many rounds?", 1, 10)
    print()

    # establishes

    rounds_played = 0

    while rounds_played < rounds:
        # output amount of rounds and guesses allowed
        round_of_rounds = as_statement("*** Round {} of {} ***".format(rounds_played + 1, rounds), "*")

        print()

        rounds_played += 1

        num = random.randint(lowest, highest)
        num1 = random.randint(lowest, highest)

        math = num + num1

        # rounds = intcheck("How many rounds?", 1, 10)  #
        question1 = intcheck("{} + {}".format(num, num1), 0, 2000)
        if question1 == math:
            print("Well done!")
            print()
            win += 1
        elif question1 != math:
            print()
            lose += 1
            print("Sorry, You Answer was Wrong!")
            print("The Answer was {}".format(math))
            print()
        result = "{} + {} : User: {}, Answer: {}".format(num, num1, question1, math)

        game_summary.append("Round #{} = {}".format(rounds_played, result))
        end.append("Game {}: Round #{} = {}".format(games_played, rounds_played, result))

    print()
    print("You have gotten to the end of the game")
    final = as_statement("### Wins:{}  |  Losses:{} ###".format(win, lose), "#")
    # End of game, Print Stats
    print()
    print("**** Game History ****")
    for item in game_summary:
        print(item)

    print()
    play_again = (input("Push <enter> to play again/continue or any other key to quit"))

print()
print("**** All Games History ****")
for thing in end:
    print(thing)
