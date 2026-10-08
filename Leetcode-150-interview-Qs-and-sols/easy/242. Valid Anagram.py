class Solution(object):
    def isAnagram(self, s, t):
        if Counter(s) == Counter(t) or sorted(s) == sorted(t):
            return True
        else:
            return False


##orr-----------------------------
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)