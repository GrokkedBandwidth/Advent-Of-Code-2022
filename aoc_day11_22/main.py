list = []
monkeys = []
inspection_values = []
monkey_mods = 1

class Monkey():
    def __init__(self):
        super(Monkey, self).__init__()
        self.name = ''
        self.inventory = []
        self.operation = ''
        self.operation_num = 0
        self.divisible_num = 0
        self.true_target = 0
        self.false_target = 0
        self.inspection = 0

    def op(self, item, operation_num):
        self.inspection += 1
        if operation_num == 'old':
            number = item
        else:
            number = int(operation_num)
        if self.operation == '*':
            return int(item) * number
        elif self.operation == '+':
            return int(item) + number

    def test(self, item, divisble_num):
        if item % divisble_num == 0:
            return True
        else:
            return False

    def transfer(self, input, t_target, f_target):
        throw = self.inventory.pop(0)
        if input:
            target = monkeys[t_target]
            target.inventory.append(throw)
        else:
            target = monkeys[f_target]
            target.inventory.append(throw)

    def worry(self, item):
        return int(int(item)/3)

with open('input.txt', mode='r') as file:
    for item in file:
        if item.strip() != '':
            list.append(item.strip())
    for num in range(0, int(len(list)/6)):
        new_monkey = Monkey()
        new_monkey.name = list[0 + (num*6)].split()[1][0]
        inventory = list[1 + (num*6)].split()[2:]
        for item in inventory:
            new_monkey.inventory.append(int(item.strip(',')))
        new_monkey.operation = (list[2 + (num*6)].split()[4])
        new_monkey.operation_num = list[2 + (num*6)].split()[5]
        new_monkey.divisible_num = int(list[3 + (num*6)].split()[3])
        new_monkey.true_target = int(list[4 + (num*6)].split()[5])
        new_monkey.false_target = int(list[5 + (num*6)].split()[5])
        monkeys.append((new_monkey))

for item in monkeys:
    monkey_mods *= item.divisible_num

for num in range(0, 10000):
    for item in monkeys:
        if item.inventory != []:
            for num in range(len(item.inventory)):
                item.inventory[0] = item.op(item=item.inventory[0], operation_num=item.operation_num)
                ## Used for Part 1 ##
                # item.inventory[0] = item.worry(item=item.inventory[0])
                item.inventory[0] = item.inventory[0] % monkey_mods
                item.transfer(input=item.test(item=item.inventory[0], divisble_num=item.divisible_num), t_target=item.true_target, f_target=item.false_target)

for item in monkeys:
    print(item.inspection)
    inspection_values.append(item.inspection)

top_1 = max(inspection_values)
inspection_values.remove(top_1)
top_2 = max(inspection_values)
monkey_business = top_2 * top_1

print(monkey_business)






