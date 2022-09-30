def numJewelsInStones(jewels: str, stones: str) -> int:
    # jewels = set(jewels)
    # return sum(s in jewels for s in stones)

    count = 0
    jSet = set()
    for jewel in jewels:
        if jewel not in jSet:
            jSet.add(jewel)

    for stone in stones:
        if stone in jSet:
            count += 1

    return 1