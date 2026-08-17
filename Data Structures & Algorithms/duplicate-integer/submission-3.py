class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # I'm converting the list into a set because
        # a set automatically keeps only unique values
        unique_nums = set(nums)

        # If the set is smaller than the original list,
        # I'm returning True because at least one duplicate was removed
        return len(unique_nums) < len(nums)