class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Calculate the occurence of char in s
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        # Take all occurence sum the char with even occurence and (odd occurence - 1)
        odd = 0
        total = 0
        for v in d.values():
            if v % 2 == 0:
                total += v
            else:
                odd = 1
                total += (v - 1)
        # We can use one odd occurence completely, so add 1 to total if odd
        # Example aaabbbccc => cbaaabc ( c- 2, b-2, a- 3)
        return (total + 1) if odd else total

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
