from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        res = 1
        for num in nums_set:
            cur_len = 1
            next_num = num + 1
            if num - 1 in nums_set:
                continue
            while next_num in nums_set:
                # 寻找序列
                cur_len += 1
                next_num += 1
            res = cur_len if cur_len > res else res

        return res

sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))