# imports a random (turned into a number and used for both questions)
import random

# checks that what the user is inputting is an integer


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


# adds 'decoration' to outputs. (Adds characters above and below statement so that statement stands out)
def as_statement(statement, char):
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""


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
    print("This Quiz is easy, answer the ")
    print("maths questions!!")
    print()
    print("For each game you can pick you")
    print("high/low numbers for your")
    print("questions")
    print()
    print("At the very end (when you quit)")
    print("you will be able to see your")
    print("whole quiz history, with stats")
    print("and everything.")
    print()
    print("---------------------------------")
    print()

# establishes that they user has not yet won, lost or played a quiz
total_right = 0
total_wrong = 0
quizzes_played = 0
questions_answered = 0

end = []  # Holds all results
stats = []  # holds all stats results

# play_again loop start
play_again = ""
while play_again == "":

    # asking the player if they would like to re-start their score
    quizzes_played += 1

    # establishes the high and low for numbers in the questions
    lowest = intcheck("Low Number: ", 0, 1000)
    highest = intcheck("High Number: ", lowest, 1000000)
    print()

    verb = ""  # empty space for later use

    quiz_summary = []  # Holds results from each round
    quiz_stats = []

    # asks user how many round they would like to play
    questions = intcheck("How many questions?", 1, 10)
    print()

    # this makes sure that the user does not answer more questions then asked for
    questions_to_be_zeroed = 0
    round_right = 0
    round_wrong = 0

    while questions_to_be_zeroed < questions:
        # output amount of questions and guesses allowed
        round_of_rounds = as_statement(" Question {} of {} ".format(questions_to_be_zeroed + 1, questions), "*")

        print()

        questions_answered += 1
        questions_to_be_zeroed += 1

        # is the import random made into a number
        num = random.randint(lowest, highest)
        num1 = random.randint(lowest, highest)

        math = num + num1

        # Asks the questions, compares the reply the answer, prints output (and correct answer if user was wrong)
        question1 = intcheck("{} + {} = ".format(num, num1), lowest, 1000000 + 1000000)
        if question1 == math:
            print("Well done!")
            print()
            round_right += 1
            verb = "Got it right"
        elif question1 != math:
            print()
            round_wrong += 1
            verb = "guessed"
            print("Sorry, You Answer was Wrong!")
            print("The Answer was {}".format(math))
            print()

        # establishes the shells for the Quiz History(s)
        if verb == "Got it right":
            result = "{} + {} = {} : You {}!".format(num, num1, math, verb, question1)
        else:
            result = "{} + {} = {} : You {} : {}".format(num, num1, math, verb, question1)

        quiz_summary.append("Question #{} : {}".format(questions_to_be_zeroed, result))
        end.append("Question #{} : {}".format(questions_answered,  result))

    total_right += round_right
    total_wrong += round_wrong

    percent_right = round_right / questions_to_be_zeroed * 100
    percent_wrong = round_wrong / questions_to_be_zeroed * 100

    print()
    print("You have gotten to the end of the quiz")

    # outputs that quizzes question+answer+right/wrong history
    print()
    print("### Quiz History ####")
    for item in quiz_summary:
        print(item)

    # makes sure that even if the user re-starts the scoreboard, the end stats have all.

    quiz_stats.append("Right: {}, ({:.0f}%)\nWrong: {}, ("
                      "{:.0f}%)".format
                      (round_right, percent_right, round_wrong, percent_wrong))

    print()
    print("#### Quiz Statistics ####")
    for item in quiz_stats:
        print(item)

    print()
    play_again = (input("Push <enter> for more questions or any other key to quit"))
    print()

# prints all info on all questions of all Quizzes.
if quizzes_played >= 2:
    print()
    print("$$$$ All Quizzes History $$$$")
    for thing in end:
        print(thing)

percent_right = total_right / questions_answered * 100
percent_wrong = total_wrong / questions_answered * 100

stats.append("Right: {}, ({:.0f}%)\nWrong: {}, ("
             "{:.0f}%)".format(total_right, percent_right, total_wrong, percent_wrong))

if quizzes_played >= 2:
    print()
    print("$$$$ ALL Quizzes Statistics $$$$")
    for item in stats:
        print(item)
