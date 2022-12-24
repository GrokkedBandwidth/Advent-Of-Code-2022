# with open('input.txt', mode='r') as file:
#     line = str(file.readline())
#     for num in range(0, len(line)):
#         if num >= 4:
#             if line[num] != line[num-3] and line[num] != line[num-2] and line[num] != line[num-1] and line[num-3] != line[num-2] and line[num-3] != line[num-1] and line[num-2] != line[num-1]:
#                 print(f'{line[num-3]}{line[num-2]}{line[num-1]}{line[num]}')
#                 print(num+1)

#### Part 2 ####

def check(list):
    comparison_list = list
    for item in list:
        count = 0
        for sub_item in comparison_list:
            if item == sub_item:
                count += 1
                if count > 1:
                    return True
    return False

with open('input.txt', mode='r') as file:
    line = str(file.readline())
    list = []
    count = 0
    for char in line:
        list.append(char)
        count += 1
        if len(list) >= 14:
            match = check(list)
            if match:
                list.reverse()
                list.pop()
                list.reverse()
            else:
                print(count)

