from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:   
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())


solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))
