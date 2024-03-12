
class Capacity:

    def __init__(self, arr, day):
        self.arr = arr
        self.day = day

    def calculate(self):
        max = 0
        sum = 0
        mean = 0
        for item in self.arr:
            if item > max:
                max = item
            sum = sum + item

        mean = (sum/self.day)
        print("mean ::", mean)
        print("max ::", max)

        if mean >= max:
            return mean + 1
        else:
            return max




arr1 = [1, 2, 1]
day1 = 2
arr2 = [9, 8, 10]
day2 = 3

17
[7, 18, 15, 15, 8, 3, 19, 8, 14, 4, 5, 14, 19, 10, 1, 1, 2]
2


capacity1 = Capacity(arr1, day1)
capacity2 = Capacity(arr2, day2)
res = capacity1.calculate()
print("result ::", res)
res = capacity2.calculate()
print("result ::", res)
