class Solution:
    def countDigitOne(self, n):
        count, col = 0, 1
        while n >= col:
            q, r = divmod(n, col * 10)
            count += q * col + min(max(r - col + 1, 0), col)
            col *= 10
        return count
