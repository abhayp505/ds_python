
def findPair(self, nums: List[int], secondDigit):
    max = len(nums) - 1
    min = 0
    target = secondDigit

    count = 0

    while (count < len(nums)):
        mid = (min + max) // 2
        if target == nums[mid]:
            return mid
        else:
            if target < nums[mid]:
                max = mid - 1
            if target > nums[mid]:
                min = mid + 1