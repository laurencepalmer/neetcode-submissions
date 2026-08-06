class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # # add one and or to make sure the bits in x are turned on
        # sol = x
        # while n - 1 > 0: 
        #     sol += 1
        #     sol = sol | x
        #     n -= 1
        #     # print(sol)

        sol = x
        i_x = 1
        i_n = 1

        while i_n < n: 
            if i_x & x == 0: 
                if i_n & (n-1):
                    sol = sol | i_x
                i_n = i_n << 1
            i_x = i_x << 1

        return sol