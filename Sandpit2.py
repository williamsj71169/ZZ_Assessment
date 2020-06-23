
def as_statement(statement, char):
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()
    return ""


games_played = 1
game_num_output = as_statement("''' Game {} '''".format(games_played), "'")
