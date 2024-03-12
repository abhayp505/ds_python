#
# Prakhar has a string with
#  words where the length of the ith word is Li
#
# The words are displayed in the window separated by a space. More precisely, when the sentence is displayed in a window of width
# W, the following conditions are satisfied.
#
# 1. The first word is displayed at the beginning of the top line.
# 2. The ith word (2 <= i <= N) is displayed either with a gap of 1 after (ith -1) the
#  word, or at the beginning of the line below the line containing the (i - 1)th word
#
# 3. The width of each line does not exceed W. Here, the width of a line refers to the distance from the left end of the leftmost word to the right end of the rightmost word.
# 2. A word should not be broken into or more lines
#
# Prakhar Wants to fit these words in M or less than M lines, find the minimum possible width
#  of the window.
#
# Input Format:
#
# The first line contains 2 space seperated integers
# N - the total number of words and
# M - the required number of lines.
#
# The next line contains N space seperated integers Li
#
# Output Format:
# Print the minimum possible width W of the window
# 6 4
# 5 4 3 6 2 4

class WordWrap:



    list_int = None
    num = None
    lines = None
    input_str = None

    def helper(self, mid):
        words = 0
        lines = 1

        for element in self.list_int:

            if words + element > mid:
                lines = lines +1
                if str(element) != " ":
                    words = element + 1
            else:
                words = words + element + 1
            print("helpher ::", element, " ", words, " ", mid, " ", lines)
        return lines


    def calculate(self):
        self.user_input()
        low_width = max(self.list_int)
        high_width = sum(self.list_int) + (self.num - 1)
        linesReq = 0
        print("inputs ::", self.list_int," ", low_width, " ", high_width)

        while low_width <= high_width:
            mid = (low_width + high_width) // 2
            print("mid ::",low_width, " ", high_width, " ", mid)
            linesReq = self.helper(mid)

            if linesReq <= self.lines:
                high_width = mid - 1
            else:
                low_width = mid + 1

        print("ans ::", low_width)

    def user_input(self):
        input1 = input("enter the 1st line::")
        list1 = list(map(int, input1.split()))
        self.num = list1[0]
        self.lines = list1[1]
        self.input_str = input("enter the 2nd line::")
        list2 = list(map(int, self.input_str.split()))
        self.list_int = list2

wr = WordWrap()
wr.calculate()



