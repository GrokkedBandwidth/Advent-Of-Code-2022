class Directory:
    def __init__(self):
        super().__init__()
        self.size = 0
        self.name = ''
        self.path = ''
        self.parent = ''
        self.contents = []

class File:
    def __init__(self):
        super().__init__()
        self.size = 0
        self.name = 'file'

def size(dir):
    total = 0
    for sub in dir.contents:
        if type(sub) == Directory:
            total += size(sub)
        else:
            total += sub.size
    return total

dirs = []
prev_dir = ''
with open('input.txt', mode='r') as file:
    current_dir = Directory()
    current_dir.name = '/'
    dirs.append(current_dir)
    path = '/'
    for item in file:
        line = item.strip().split()
        if line[1] == 'cd':
            if line[2] != '..' and line[2] != '/':
                for subitem in dirs:
                    if subitem.name == line[2]:
                        current_dir = subitem
                        path += current_dir.name
            else:
                name = current_dir.parent
                for subitem in dirs:
                    if subitem.name == name:
                        current_dir = subitem
        elif line[0] == 'dir':
            new_dir = Directory()
            new_dir.name = line[1]
            dirs.append(new_dir)
            new_dir.path += f'{current_dir.name}/'
            new_dir.parent = current_dir.name
            current_dir.contents.append(new_dir)
        elif line[0] != '$':
            new_file = File()
            new_file.size = int(line[0])
            current_dir.contents.append(new_file)
            current_dir.size += int(line[0])

for item in dirs:
    item.size = size(item)

total = 0
for item in dirs:
    print(item.name)
    print(item.size)
print(total)


