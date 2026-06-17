class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[0]*2*len(nums)
        for i, num in enumerate(nums):
            arr[i]=arr[len(nums)+i]=num
        return arr
        