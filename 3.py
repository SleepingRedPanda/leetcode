def lengthOfLongestSubstring(s: str) -> int:
    count = 0
    start = max_length = 0
    char_frequency = {}
    for i, char in enumerate(s):
        if char in char_frequency and start <= char_frequency[char]:
            start = char_frequency[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        char_frequency[char] = i


    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))