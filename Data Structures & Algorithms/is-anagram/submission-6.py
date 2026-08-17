class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I'm creating two dictionaries to store
        # the frequency of each character in both strings
        s_map = {}
        t_map = {}

        # I'm checking the lengths first because
        # anagrams must have the same number of characters
        if len(s) != len(t):
            return False

        # I'm going through both strings at the same time
        for i in range(len(s)):

            # I'm counting each character from the first string
            s_map[s[i]] = 1 + s_map.get(s[i], 0)

            # I'm counting each character from the second string
            t_map[t[i]] = 1 + t_map.get(t[i], 0)

        # I'm comparing both frequency dictionaries
        # If they are equal, the strings are anagrams
        return s_map == t_map
            