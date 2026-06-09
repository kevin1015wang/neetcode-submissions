class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countArr = [0,0,0]

        for num in nums:
            countArr[num] += 1
        
        currIndex = 0

        for i in range(len(countArr)):
            for j in range(countArr[i]):
                nums[currIndex] = i
                currIndex += 1
        
        return nums
        