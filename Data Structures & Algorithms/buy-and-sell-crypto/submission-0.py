class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L , R = 0 , 1
        out = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                res = prices[R] - prices[L]
                out = max(out,res)
            else:
                L = R
            R += 1
        return out
