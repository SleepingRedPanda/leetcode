def longestNiceSubstring(s: str) -> str:
    ans = ""
    for i in range(len(s)):
        for j in range(i):
            ss = s[j:i+1]
            if set(ss) == set(ss.swapcase()):
                ans = max(ans, ss, key=len)
    return ans

s = "Bb"
print(longestNiceSubstring(s))
# [Bb]