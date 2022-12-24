class Directory:
    def __init__(self):
        super().__init__()
        self.size = 0
        self.name = ''
        self.parent = ''
        self.contents = []

class File:
    def __init__(self):
        super().__init__()
        self.size = 0

dir = []
new_file = File()
new_file.name = 'name'
dir.append(new_file)
for item in dir:
    if item.name == 'name':
        x = item
        print(x)