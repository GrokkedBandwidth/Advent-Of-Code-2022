values = []
strength = []
clock_cycle = 0
register = 1
screen = ''
sprite_positions = []
round = 0

def clock_check(cycle, register):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        return cycle * register
    else:
        return 0

def sprite_check(cycle, register):
    global round
    if register - 1 <= cycle - (40 * round) <= register + 1:
        sprite_positions.append('#')
    else:
        sprite_positions.append('.')

def inc_round(cycle):
    global round
    if cycle % 40 == 0:
        round += 1

with open('input.txt', mode='r') as file:
    for item in file:
        line = item.strip().split()
        command = line[0]
        if command == 'noop':
            pass
        elif command == 'addx':
            number = int(line[1])
            values.append(number)
            clock_cycle += 1
            inc_round(cycle=clock_cycle)
            sprite_check(cycle=clock_cycle, register=register)
            strength.append(clock_check(cycle=clock_cycle, register=register))
            register += values[-1]
        clock_cycle += 1
        inc_round(cycle=clock_cycle)
        sprite_check(cycle=clock_cycle, register=register)
        strength.append(clock_check(cycle=clock_cycle, register=register))
    print(f'Total Signal Strength: {sum(strength)}')

for num in range(1, 241):
    screen += sprite_positions[num-1]
    if num % 40 == 0:
        screen += '\n'

print(screen)








