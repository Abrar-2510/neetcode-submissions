class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag_count = Counter(magazine)

        for char in ransomNote:
            if mag_count[char] <= 0:
                return False
            
            mag_count [char] -= 1
        return True
        