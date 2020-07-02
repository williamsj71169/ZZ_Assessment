


print("Win: {}, ({:.0f}%)\nLoss: {}, ("
      "{:.0f}%)\nTie: {}, ({:.0f}%)".format
      (win, percent_win, lose, percent_lose, tie, percent_tie))

percent_win = win / rounds_played * 100
percent_lose = lose / rounds_played * 100