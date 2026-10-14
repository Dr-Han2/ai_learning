"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_len = 0
    window = set()

    for right, ch in enumerate(s):
        while ch in window:
            window.remove(s[left])
            left += 1

        window.add(ch)
        max_len = max(max_len, right - left + 1)

    return max_len
print(lengthOfLongestSubstring("abcabcbb"))