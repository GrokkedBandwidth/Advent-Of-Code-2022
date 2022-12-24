score = 0

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

with open('input.txt', mode='r') as file:
    for item in file:
        if item[0] == ROCK:
            if item[2] == 'Y':
                score += 3
                score += 1
            elif item[2] == 'X':
                score += 3
            elif item[2] == 'Z':
                score += 2
                score += 6
        elif item[0] == PAPER:
            if item[2] == 'Y': #paper
                score += 2
                score += 3
            elif item[2] == 'X': #rock
                score += 1
            elif item[2] == 'Z': #scissors
                score += 3
                score += 6
        elif item[0] == SCISSORS:
            if item[2] == 'Y':
                score += 3
                score += 3
            elif item[2] == 'X':
                score += 2
            elif item[2] == 'Z':
                score += 1
                score += 6

print(score)