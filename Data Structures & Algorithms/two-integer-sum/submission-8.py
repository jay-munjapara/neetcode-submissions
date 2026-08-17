class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating a dictionary to keep the numbers 
        # I have already seen along with thier indices
        seen = {}
        
        # using enumerate so I can access both the value and its index
        for index, num in enumerate(nums):
            # calculating the number I need to reach the target
            needed = target - num

            if needed in seen:
                # returning the sotred intex along with my current index
                return [seen[needed], index]
            # storing the current number so that I don't use the same element twice
            seen[num] = index
'''
Explanation:
- I have used a dictionary for previously seen numbers
- I used it since lookup is approximately O(1)
- Calculate: needed = target - num
- Check whether needed is already in seen
- If yes, return both indices
- Else, store the current number
- Check before storing to avoid using the same element twice
- In my opinion, this is optimal:
- Time: O(n)
- Space: O(n)
'''

'''
Explanation: I used a dictionary to store previously seen numbers and
their indices, allowing me to find the required complement 
efficiently and solve the problem in O(n) time.
'''

















