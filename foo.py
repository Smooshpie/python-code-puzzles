x = ["H", "e", "l", "l", "o", "", "W", "o", "r", "l", "d", "!"]

for idx, letter in enumerate(x):
    if(idx != len(x) - 1):
        print(letter, end="")
    else:
        print(letter, end="\n")