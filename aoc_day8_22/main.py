line = []
score = 0
height = 0
visibility = []

def check_top(current_num, num, line, height):
    global top
    count = 0
    top = 1
    for subnum in range(height - 1, -1, -1):
        if current_num > int(line[subnum][num]):
            count += 1
            top += 1
            if count >= height:
                top -=1
                return True
        else:
            return False


def check_bottom(current_num, num, line, height):
    global bottom
    count = height + 1
    bottom = 1
    for subnum in range(height + 1, len(line)):
        if current_num > int(line[subnum][num]):
            count += 1
            bottom += 1
            if count >= len(line):
                bottom -= 1
                return True
        else:
            return False


def check_right(current_num, line, length, height):
    global right
    count = length + 1
    right = 1
    for subnum in range(length + 1, len(line[0])):
        if current_num > int(line[height][subnum]):
            count += 1
            right += 1
            if count >= len(line[0]):
                right -= 1
                return True
        else:
            return False


def check_left(current_num, line, length, height):
    global left
    count = 0
    left = 1
    for subnum in range(length - 1, -1, -1):
        if current_num > int(line[height][subnum]):
            count += 1
            left += 1
            if count >= length:
                left -= 1
                return True
        else:
            return False


with open('input.txt', mode='r') as file:
    for item in file:
        line.append(item.strip())
    for item in line:
        for num in range(0, len(item)):
            current_number = int(item[num])
            if num == 0 or num == len(item) - 1:
                score += 1
            elif item == line[0] or item == line[len(line)-1]:
                score += 1
            else:
                check1 = check_top(current_num=current_number, num=num, line=line, height=height)
                check2 = check_bottom(current_num=current_number, num=num, line=line, height=height)
                check3 = check_left(current_num=current_number, line=line, length=num, height=height)
                check4 = check_right(current_num=current_number, line=line, length=num, height=height)
                if check4 or check3 or check2 or check1:
                    score += 1
                visibility.append(top*left*right*bottom)
        height += 1

print(score)
print(max(visibility))















