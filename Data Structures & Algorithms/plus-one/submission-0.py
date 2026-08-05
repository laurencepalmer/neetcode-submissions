class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        top = 1
        res = 0
        nums = []
        for i in range(len(digits)-1, -1, -1): 
            res = digits[i] + top
            top = res // 10
            res = res % 10
            nums.insert(0, str(res))

        if top > 0: 
            nums.insert(0, top)

        return nums