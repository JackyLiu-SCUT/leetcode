from typing import List
import pdb

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 暴力生成，逐一验证
        
        # 递归生成
        def generate(A):
            print("sdgfasf")
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                print(A)
                # pdb.set_trace()
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        # pdb.set_trace()
        generate([])
        # pdb.set_trace()
        return ans

sol = Solution()
print(sol.generateParenthesis(3))