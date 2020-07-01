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
    print("For each game you can pick you high/low")
    print("numbers for your questions")
    print("At the start of a new 'quiz' you can choose ")
    print("to continue with your previous scores or ")
    print("start anew.")
    print()
    print("---------------------------------")

# establishes that they user has not yet won, lost or played a quiz
right = 0
wrong = 0
quizzes_played = 0
questions_answered = 0

end = []  # Holds all results

# play_again loop start
play_again = ""
while play_again == "":

    # asking the player if they would like to re-start their score
    quizzes_played += 1
    if quizzes_played > 1:
        print("")
        yes_no = yn_checker("Would you like to re-start your score board? ")
        if yes_no == "Yes":
            losses = 0
            wins = 0

    # establishes the high and low for numbers in the questions
    lowest = intcheck("Low Number: ", 0, 100)
    highest = intcheck("High Number: ", lowest, 100000)
    print()

    verb = ""

    quiz_summary = []  # Holds results from each round

    # asks user how many round they would like to play
    questions = intcheck("How many questions?", 1, 10)
    print()

    questions_to_be_zeroed = 0

    while questions_to_be_zeroed < questions:
        # output amount of questions and guesses allowed
        round_of_rounds = as_statement(" Question {} of {} ".format(questions_answered + 1, questions), "*")

        print()

        questions_answered += 1

        # is the import random made into a number
        num = random.randint(lowest, highest)
        num1 = random.randint(lowest, highest)

        math = num + num1

        # Asks the questions, compares the reply the answer, prints output (and correct answer if user was wrong)
        question1 = intcheck("{} + {} = ".format(num, num1), lowest, highest + highest)
        if question1 == math:
            print("Well done!")
            print()
            right += 1
            verb = "Got it right"
        elif question1 != math:
            print()
            wrong += 1
            verb = "guessed"
            print("Sorry, You Answer was Wrong!")
            print("The Answer was {}".format(math))
            print()

        # establishes the shells for the Quiz History(s)
        if verb == "Got it right":
            result = "{} + {} = {} : You {}!".format(num, num1, math, verb, question1)
        else:
            result = "{} + {} = {} : You {} : {}".format(num, num1, math, verb, question1)
        quiz_summary.append("Question #{} : {}".format(questions_answered, result))
        end.append("Question #{} : {}".format(questions_answered,  result))

    print()
    print("You have gotten to the end of the quiz")

    final = as_statement("### Right:{}  |  Wrong:{} ###".format(right, wrong), "#")
    # End of quiz, Print Stats
    print()
    print("**** Quiz History ****")
    for item in quiz_summary:
        print(item)

    print()
    play_again = (input("Push <enter> for more questions or any other key to quit"))
    print()

# prints all info on all questions of all Quizzes.
if quizzes_played >= 2:
    print()
    print("**** All Quizzes History ****")
    for thing in end:
        print(thing)
