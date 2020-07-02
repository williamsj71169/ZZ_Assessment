# start of game

total_right = 0
total_wrong = 0

keep_going = ""
while keep_going == "":
    num_right = 0
    num_wrong = 0

    how_many = int(input("rounds: "))

    for item in range(0, how_many):

        result = input("result? " )

        if result == "right":
            num_right += 1
        else:
            num_wrong += 1

    print()
    print("Right: ", num_right)
    print("wrong: ", num_wrong)

    total_right += num_right
    total_wrong += num_wrong

print()
print("Total right: ", total_right)
print("total wrong: ", total_wrong)