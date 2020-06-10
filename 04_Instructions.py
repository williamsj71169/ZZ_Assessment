

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
