# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team
# 2, the third goes into team 1, and so on.

def rowWeights(teamlist):
    team1 = teamlist[::2]
    team2 = teamlist[1::2]

    sumteam1 = sum(team1)
    sumteam2 = sum(team2)

    return (sumteam1, sumteam2)


print(rowWeights([13, 27, 49]))  # (62, 27)
