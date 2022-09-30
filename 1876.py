def countGoodSubstrings(s: str) -> int:
    # s = list(s)
    # count = 0
    # k = 3
    # sub_s = []
    #
    # if len(s) == 0 and len(s) < k:
    #     return count
    #
    # for i in range(k):
    #     sub_s.append(s[i])
    # if len(set(sub_s)) == 3:
    #     count += 1
    #
    # for i in range(k, len(s)):
    #     sub_s.pop(0)
    #     sub_s.append(s[i])
    #     if len(set(sub_s)) == 3:
    #         count += 1
    # return count

    count = 0
    k = 3
    for i in range(len(s)-2):
        if len(set(s[i:i+k])) == 3:
            count += 1
    return count
print(countGoodSubstrings("xay"))