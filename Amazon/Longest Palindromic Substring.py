'''
5. Longest Palindromic Substring
Input: s = "babad"
Output: "bab"
'''


def longestPalindrome(s: str) -> str:
    n = len(s)
    res = s[0]
    for i in range(1, n):
        # even palindrome check
        # example --> 'abba' -> mid = right 'b', left = left 'b'. starting from these two positions
        # now keep stretching until the characters dont match.
        # finally check if the string got is max
        mid = i
        left = i-1

        while mid < n and left >= 0 and s[mid] == s[left]:
            mid += 1
            left -= 1
        res = max(res, s[left+1:mid], key=lambda x: len(x))
        # odd palindrome check
        # example --> cabad, if i points to b, then left points to left 'a' or i-1
        # and right points to right 'a' or i+1.
        # now stretch until the characters dont match and find max
        left = i-1
        right = i+1
        print(f"Outside Right: mid {mid} and left {left}")
        while left >= 0 and right < n and s[left] == s[right]:
            print(f"While Right: mid {mid} and left {left}")
            left -= 1
            right += 1
        res = max(res, s[left+1:right], key=lambda x: len(x))
    return res


print(longestPalindrome("babad"))
