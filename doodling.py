example = "A man, a plan, a canal: Panama"
palindromeCheck = ""
for i in example:
    if i.isalnum:
        palindromeCheck += i

palindromeCheck = palindromeCheck.lower()



print(palindromeCheck)