score = 0

# with open('input.txt', mode='r') as file:
#     for item in file:
#         line = item.strip().split(',')
#         elf_1 = line[0].split('-')
#         elf_2 = line[1].split('-')
#         if int(elf_1[0]) <= int(elf_2[0]) and int(elf_1[1]) >= int(elf_2[1]):
#             score += 1
#         elif int(elf_2[0]) <= int(elf_1[0]) and int(elf_2[1]) >= int(elf_1[1]):
#             score += 1

#### Part 2 ####

with open('input.txt', mode='r') as file:
    for item in file:
        line = item.strip().split(',')
        elf_1 = line[0].split('-')
        elf_2 = line[1].split('-')
        if int(elf_1[0]) <= int(elf_2[1]) and int(elf_1[1]) >= int(elf_2[0]):
            score += 1
            print(line)
        elif int(elf_2[0]) <= int(elf_1[1]) and int(elf_2[1]) >= int(elf_1[0]):
            score += 1
            print(line)


print(score)