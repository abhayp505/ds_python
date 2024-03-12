
newString = ""
def validPalindrom(phrase: str, length):
    phrase = phrase.replace(" ", "")
    print("pharse ::", phrase)
    global newString
    uniq = set()
    if length >0:
        uniq.add(phrase[length-1])
        newString = newString+phrase[length-1]
        return validPalindrom(phrase, length-1)
    else:
        len(uniq)
        return newString


phrase = "AmanaplanacanalPanama"
vp = validPalindrom(phrase, len(phrase))
print("vp ::", vp)