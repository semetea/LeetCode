class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        initialNum = 0
        for val in nums:
            initialNum = initialNum + val
            runningSum.append(initialNum)
        return runningSum

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
