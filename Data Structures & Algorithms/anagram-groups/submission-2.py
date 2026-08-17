class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I'm creating a dictionary where each sorted word
        # will map to a list of its matching anagrams
        ans = collections.defaultdict(list)

        # I'm going through each string in the input
        for s in strs:

            # I'm sorting the characters to create a common key
            # For example: "eat", "tea", and "ate" all become "aet"
            k = "".join(sorted(s))

            # I'm adding the original string to its matching anagram group
            ans[k].append(s)

        # I'm returning only the grouped anagram lists
        return list(ans.values())