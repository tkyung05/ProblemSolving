import sys
input = sys.stdin.readline

string = list(map(str, input().strip('\n')))

tag = False
word_trig = False

result = []
word = []

for i in range(len(string)):
    if string[i] == '>':
        tag = False
        result.append(string[i])
        continue

    if tag:
        result.append(string[i])
        continue
    
    if string[i] == '<':
        if word_trig:
            for _ in range(len(word)):
                result.append(word.pop())
            word_trig = False
        tag = True
        result.append(string[i])
        continue

    if i == len(string) - 1 and word_trig:
        word.append(string[i])
        for _ in range(len(word)):
            result.append(word.pop())
        continue

    if string[i] == ' ' and word_trig:
        for _ in range(len(word)):
            result.append(word.pop())
        result.append(string[i])
        word_trig = False
        continue

    word.append(string[i])
    word_trig = True

print(''.join(result))
