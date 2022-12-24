# rows = []
# height = 0
# with open('input.txt', mode='r') as file:
#     for item in file:
#         try:
#             height += 1
#             if item[1] == '1':
#                 column_num = int(max(item.strip().split()))
#                 break
#         except IndexError:
#             continue
#     for num in range(0, column_num):
#         column = []
#         rows.append(column)
#     file.readline()
#     instructions = file.readlines()
#
# with open('input.txt', mode='r') as file:
#     for num in range(0, height-1):
#         line = file.readline().replace('[', '').replace(']','').replace('    ',',').replace(' ',',').strip().split(sep=',')
#         count = 0
#         print(line)
#         for item in line:
#             if item == '':
#                 count += 1
#             else:
#                 rows[count].append(item)
#                 count += 1
#     for item in rows:
#         item.reverse()
#
# print(instructions)
# for item in instructions:
#     for num in range(0, int(item.strip().split()[1])):
#         crate = rows[int(item.strip().split()[3])-1].pop()
#         rows[int(item.strip().split()[5])-1].append(crate)
#
#
# print(rows)

#### Part 2 ####

rows = []
height = 0
with open('input.txt', mode='r') as file:
    for item in file:
        try:
            height += 1
            if item[1] == '1':
                column_num = int(max(item.strip().split()))
                break
        except IndexError:
            continue
    for num in range(0, column_num):
        column = []
        rows.append(column)
    file.readline()
    instructions = file.readlines()

with open('input.txt', mode='r') as file:
    for num in range(0, height-1):
        line = file.readline().replace('[', '').replace(']','').replace('    ',',').replace(' ',',').strip().split(sep=',')
        count = 0
        print(line)
        for item in line:
            if item == '':
                count += 1
            else:
                rows[count].append(item)
                count += 1
    for item in rows:
        item.reverse()

for item in instructions:
    crate_load = []
    for num in range(0, int(item.strip().split()[1])):
        crate = rows[int(item.strip().split()[3])-1].pop()
        crate_load.append(crate)
    crate_load.reverse()
    for crate in crate_load:
        rows[int(item.strip().split()[5]) - 1].append(crate)

print(rows)
