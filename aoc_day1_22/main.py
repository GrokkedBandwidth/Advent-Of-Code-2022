list = []

with open('input.txt', mode='r') as file:
    for number in file:
        list.append(number.strip())

value = 0
elves = []

for item in list:
    if item != '':
        value += int(item)
    else:
        elves.append(value)
        value = 0

one = max(elves)
elves.remove(max(elves))
two = max(elves)
elves.remove(max(elves))
three = max(elves)
elves.remove(max(elves))

total = one + two + three
print(total)





