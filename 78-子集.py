from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = []
        n = len(nums)

        def backtrack(cur, n):
            if cur == n:
                temp = [i for i in stack]
                ans.append(temp)
                return

            # 考虑当前位置
            stack.append(nums[cur])
            backtrack(cur+1, n)
            stack.pop()
            # 不考虑当前位置
            backtrack(cur+1, n)

        backtrack(0, n)
        return ans

sol = Solution()
print(sol.subsets([1,2,3,4,5,6,7,8,10,0]))