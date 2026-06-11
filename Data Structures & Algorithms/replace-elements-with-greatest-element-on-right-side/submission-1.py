class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #right max is -1 the max
        # traverse the array from right to left
        #update new max

        rightMax=-1

        for i in range(len(arr)-1, -1, -1):
            newMax=max(arr[i], rightMax)
            arr[i]=rightMax
            rightMax=newMax

        return arr
      
        