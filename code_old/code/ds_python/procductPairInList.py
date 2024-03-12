# User function Template for python3

class Solution:
    def __init__(self):
        print("inside class")

    def isProduct(self, arr, n, x):
        # code here
        for i in arr:
            if x == 0:
                if 0 in arr:
                    return True
            if i == 0:
                continue
            if i <= (x / 2):
                if x % i == 0:
                    product = x / i
                    if product in arr:
                        return True
            else:
                continue
        return False

# {
# Driver Code Starts
# Initial Template for Python 3


ob = Solution()
n= 4
x = 500
arr = [10, 20, 9, 40]
ans = ob.isProduct(arr, n, x)
print(ans)

'''if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n= 4
        x = 400 #list(map(int, input().strip().split()))
        arr = [10, 20, 9, 40]#list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.isProduct(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends'''
