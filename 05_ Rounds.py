
rounds = intcheck("How many rounds?", 1, 10)
print()

rounds_played = 0

while rounds_played < rounds:
    # output amount of rounds and guesses allowed
    print("Round {} of {}".format(rounds_played + 1, rounds))
    print()

    rounds_played += 1
