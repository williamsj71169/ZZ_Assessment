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

lowest = 0
highest = 1000


num = random.randint(lowest, highest)
num1 = random.randint(lowest, highest)


math = num + num1

game_summary = []  # Holds results from each round


rounds_played = 0


question1 = intcheck("{} + {} = ".format(num, num1), 1, 100)

result = "{} + {} : User: {}, Answer: {}".format(num, num1, question1, math)


game_summary.append("Round #{} = {}".format(rounds_played, result))

# End of game, Print Stats
print()
print("**** Game History ****")
for item in game_summary:
    print(item)
