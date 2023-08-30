word = []

chars = input()

for i in range(len(chars)):
    char = chars[i]

    if(char == "<"):
        if(len(word) != 0):
            word.pop()
    else:
        word.append(char)

print("".join(word))