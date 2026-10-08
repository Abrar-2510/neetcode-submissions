
class Solution(object):
    def removeDuplicates(self, nums):
        k=len(nums)
        nums[:]=sorted(set(nums))
        return k


#--------------------------------------------------------

class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i



