class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        counter = 0

        for i in range (len(nums)):
            if val != nums[i]:
                nums[counter] = nums[i]
                counter += 1

        return counter




        