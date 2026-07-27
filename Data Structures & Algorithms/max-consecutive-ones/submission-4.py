class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxall=0
        
        currmax=0
        for i in range(len(nums)):
            if nums[i]==1:
                currmax+=1
                maxall=max(currmax, maxall)

            else:
                currmax=0
        return maxall

        