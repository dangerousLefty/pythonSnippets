def lengthOfLastWord(s: str) -> int:
    count = 0
    switch = False

    for char in s[::-1]:
        if char != ' ':
            count += 1
            switch = True
        elif switch:
            break
    return count


s = "   fly me   to   the moon  "
j = ["apple", "banana", "cherry"]
print(j[0][3])
