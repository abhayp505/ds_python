

class LongestPalindromicStr:

    def __init__(self, inputString):
        self.inputString = inputString

    def subString(self, data ):
        subStringList = data.split(" ")
        print(subStringList)
        return subStringList

    def Ispalindrom(self, words):
        length = (len(words)-1)
        #print("length words ::", length)
        for x in range(int(length/2)+1):
            if words[x] == words[length-x]:
                continue
            else:
                return False
        return True

    def largestSubsting(self):
        length = 0
        result = ""
        wordList = self.subString(self.inputString)
        for words in wordList:
            if len(words) > length:
                print("to check ::", words)
                if self.Ispalindrom(words):
                    length = len(words)
                    result = words
                    print("palindrom ::", words)
                    print("palindrom length::", length)
            else:
                continue
        return result

input = """Evaluate maydyam the valueeulav of an arithmetic expressionnoisserpxe in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand maydyam be anna integer or another anotherrehtona expression."""
input2 = 'anotherrehtona'
obj = LongestPalindromicStr(input)
#obj.subString()
#result = obj.Ispalindrom(input2)
result = obj.largestSubsting()
print("result ::", result)