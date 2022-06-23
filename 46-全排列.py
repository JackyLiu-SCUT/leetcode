from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = []
        n = len(nums)

        def backtrack():
            # global ans
            # global stack
            if len(stack) == n:
                ans.append([i for i in stack])
                # print(ans)
                return ans

            for i in range(len(nums)):
                if nums[i] is not None:
                    stack.append(nums[i])
                    nums[i] = None
                    backtrack()
                    nums[i] = stack.pop()

        backtrack()
        return ans

sol = Solution()
print(sol.permute([1,2,3]))