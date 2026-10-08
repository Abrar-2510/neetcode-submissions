class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        mapping = {}
        used_chars = set()
        
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            else:
                if c2 in used_chars:  # already mapped by another char
                    return False
                mapping[c1] = c2
                used_chars.add(c2)
        
        return True