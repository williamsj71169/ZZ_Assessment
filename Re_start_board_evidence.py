
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

losses = 10
wins = 10

print(losses)
print(wins)


quizzes_played = 2

quizzes_played += 1
if quizzes_played > 1:
    print("")
    yes_no = yn_checker("Would you like to re-start your score board? ")
    if yes_no == "Yes":
        losses = 0
        wins = 0

print(losses)
print(wins)