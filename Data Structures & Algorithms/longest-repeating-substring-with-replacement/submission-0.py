class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        out = 0

        L = 0
        maxf = 0
        for R in range(len(s)):
            counter[s[R]] = counter.get(s[R] , 0) + 1
            maxf = max(maxf , counter[s[R]])

# the res will never change because if it change than the maxf has to increment 
# so dont need to change the maxf by going throughthe whole hash map(O(26n))

            while (R-L+1) - maxf > k: 
                counter[s[L]] -= 1
                L += 1

            out = max(out , R-L+1)

        return out