# A: Rock
# B: Paper
# C: Scissors
# X: Rock
# Y: Paper
# Z: Scissors

WIN =  6
DRAW = 3
LOSE = 0

shape_score = {"X":1, "Y":2, "Z":3}

opponent_vs_me = {("A","X"):DRAW, ("A","Y"):WIN, ("A","Z"):LOSE,
                    ("B","X"):LOSE, ("B","Y"):DRAW, ("B","Z"):WIN,
                    ("C","X"):WIN, ("C","Y"):LOSE, ("C","Z"):DRAW}



with open("data.txt", "r") as f:
    lines = f.readlines()

games = [tuple(line.strip().split(" ")) for line in lines]
game_scores = [opponent_vs_me[game] + shape_score[game[1]] for game in games]

game_sum = sum(game_scores)
print(game_sum)
                     