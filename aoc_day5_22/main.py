column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []
column8 = []
column9 = []
index = 0

def remove_space(column):
    for item in column:
        if item == ' ':
            column.remove(' ')

with open('input.txt', mode='r') as file:
    lines = file.readlines()
    for item in lines:
        index += 1
        if item[1] != '1':
            try:
                column1.append(f'{item[1]}')
                column2.append(f'{item[5]}')
                column3.append(f'{item[9]}')
                column4.append(f'{item[13]}')
                column5.append(f'{item[17]}')
                column6.append(f'{item[21]}')
                column7.append(f'{item[25]}')
                column8.append(f'{item[29]}')
                column9.append(f'{item[33]}')
            except IndexError:
                continue
        else:
            break

remove_space(column1)
remove_space(column2)
remove_space(column3)
remove_space(column4)
remove_space(column5)
remove_space(column6)
remove_space(column7)
remove_space(column8)
remove_space(column9)
column1.reverse()
column2.reverse()
column3.reverse()
column4.reverse()
column5.reverse()
column6.reverse()
column7.reverse()
column8.reverse()
column9.reverse()
rows = []
rows.append('')
rows.append(column1)
rows.append(column2)
rows.append(column3)
rows.append(column4)
rows.append(column5)
rows.append(column6)
rows.append(column7)
rows.append(column8)
rows.append(column9)

for item in lines:
    row = item.split()
    try:
        if row[0] == 'move':
            for num in range(0, int(row[1])):
                crate = rows[int(row[3])].pop()
                rows[int(row[5])].append(crate)
    except IndexError:
        continue




print(column1)
print(column2)
print(column3)
print(column4)
print(column5)
print(column6)
print(column7)
print(column8)
print(column9)
