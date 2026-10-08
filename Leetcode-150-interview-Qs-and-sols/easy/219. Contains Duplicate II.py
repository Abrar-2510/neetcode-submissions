class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        nums_map = {}

        for i in range(len(nums)):
            if nums[i] in nums_map:
                if i - nums_map[nums[i]] <= k:
                    return True
            
            # update latest index
            nums_map[nums[i]] = i
        
        return False