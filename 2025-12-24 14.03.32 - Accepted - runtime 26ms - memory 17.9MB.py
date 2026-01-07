class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        count = 0
        for c in s:
            if c == '1':
                count += 1
                result = (result + count) % MOD
            else:
                count = 0
        return result