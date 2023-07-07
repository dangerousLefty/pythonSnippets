def romanToInt(s: str) -> int:
    sum = 0
    # find the first element
    first = s[0]
    match first:
        case 'I':
            sum += 1
        case 'V':
            sum += 5
        case 'X':
            sum += 10
        case 'L':
            sum += 50
        case 'C':
            sum += 100
        case 'D':
            sum += 500
        case 'M':
            sum += 1000

    if len(s) > 1:
        # perform calculations on the rest of s
        for charIndex in range(1, len(s)):
            match s[charIndex]:
                case 'I':
                    sum += 1
                case 'V':
                    if s[charIndex-1] == 'I':
                        sum += 4
                    sum += 5
                case 'X':
                    if s[charIndex-1] == 'I':
                        sum += 9
                    sum += 10
                case 'L':
                    if s[charIndex-1] == 'X':
                        sum += 40
                    sum += 50
                case 'C':
                    if s[charIndex-1] == 'X':
                        sum += 90
                    sum += 100
                case 'D':
                    if s[charIndex-1] == 'C':
                        sum += 400
                    sum += 500
                case 'M':
                    if s[charIndex-1] == 'C':
                        sum += 900
                    sum += 1000

    return sum


romanNumeral = "XIV"
num = romanToInt(romanNumeral)
