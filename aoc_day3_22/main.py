priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}
# score = 0
# with open('input.txt', mode='r') as file:
#     for item in file:
#         word_length = int(len(item.strip())/2)
#         word_1 = item[:word_length]
#         word_2 = item[word_length:]
#         count = 0
#         for num in range(0, word_length):
#             for char in range(0, word_length):
#                 if word_1[num] == word_2[char] and count != 1:
#                     score += priorities[word_1[num]]
#                     count = 1

#### Part 2 ####

score = 0
with open('input.txt', mode='r') as file:
    for num in range(0, 300, 3):
        item_1 = file.readline().strip()
        item_2 = file.readline().strip()
        item_3 = file.readline().strip()
        count = 0
        for i in range(0, len(item_1)):
            for j in range(0, len(item_2)):
                for w in range(0, len(item_3)):
                    if item_1[i] == item_2[j] and item_1[i] == item_3[w] and count != 1:
                        count = 1
                        score += priorities[item_1[i]]



print(score)