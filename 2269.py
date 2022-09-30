def divisorSubstrings(num: int, k: int) -> int:
    l = 0
    r = k
    num = str(num)
    count = 0

    while r <= len(num):
        n = int(num[l:r])
        print(n)
        if not n:
            l += 1
            r += 1
            continue
        if int(num) % n == 0:
            count += 1
        l += 1
        r += 1
    return count


num = 430043
k = 2
print(divisorSubstrings(num, k))