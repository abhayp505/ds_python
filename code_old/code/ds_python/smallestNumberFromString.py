from stack import pop, push, stacks, length

class SmallestNumber:

    def removeKChar(self, series: str, k: int):

        if k == 0:
            return series

        if len(series) <= k:
            return '0'
        count = 0
        pointer = 0
        size = len(series)
        
        while k > 0 and count < size:
            element = int(series[count])

            if count == 0:
                pointer = push(element)
            else:
                if element == 0:
                    pop()
                    k=k-1
                elif pointer > element:
                    pop()
                    k=k-1
                    pointer = push(element)
                elif pointer < element and count == size-1:
                    k=k-1
                else:
                    pointer = push(element)
            count = count+1
        newStr = ''
        print("stack ::", stacks(), " :: ", series[count: ])
        for ele in stacks():
            newStr = newStr + str(ele)
        newStr = newStr + series[count: ]
        print("new string ::", newStr)


sm = SmallestNumber()
series = '765028321'
sm.removeKChar(series, 4)

