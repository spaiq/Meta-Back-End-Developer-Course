def isPalindrome(word):
    startIndex = 0
    endIndex = len(word) - 1

    for x in range(int(len(word)/2)):
        if word[startIndex] != word[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
       
    return True


print(isPalindrome("racecar"))
