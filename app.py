str = "3#1234#45679#890101010"

outputArr = list()
i = 0
while i < len(str):
    if str[i].isdigit() and str[i+1] == '#':
        length = int(str[i])
        outputArr.append(str[i+2: i+2 + length])
        i = i + 2 + length
    
    else:
        i += 1