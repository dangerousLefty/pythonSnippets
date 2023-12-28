def isPalindrome(s: str) -> bool:
    palindromeCheck = ""

    for i in s:
        if not i.isalnum:
            continue
        else:
            palindromeCheck += i.lower()
        
    palindromeReverse = palindromeCheck[::-1]

    if palindromeCheck == palindromeReverse:
        return True
    else:
        return False


a = isPalindrome("A man, a plan, a canal: Panama")

b = dict()