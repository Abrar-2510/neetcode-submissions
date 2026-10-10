class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            seen = {}

            for word in strs:
                if i >= len(word):
                    return prefix

                char = word[i]
                seen[char] = seen.get(char, 0) + 1

            if len(seen) == 1:
                prefix += strs[0][i]
            else:
                return prefix

        return prefix