from typing import List

# # DP
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)

#         f_list = [nums[0]]
#         pre = nums[0]

#         for i in range(1, n):
#             pre = max(nums[i], pre + nums[i])
#             f_list.append(pre) 
#         print(f_list)
#         return max(f_list)



# 分治
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.get(nums, 0, len(nums) - 1)[2]

    def get(self, nums, l, r):
        if l == r:
            return [nums[l]] * 4

        m = (l+r) >> 1
        left = self.get(nums, l, m)
        right = self.get(nums, m + 1, r)
        return self.pushUp(left, right)

    def pushUp(self, left, right):
        
        # left: [lSum, rSum, mSum, iSum]
        iSum = left[3] + right[3]
        lSum = max(left[0], left[3] + right[0])
        rSum = max(right[1], right[3] + left[1])
        mSum = max(left[2], right[2], left[1] + right[0])
        
        return [lSum, rSum, mSum, iSum]

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))