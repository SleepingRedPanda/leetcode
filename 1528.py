def restoreString(s: str, indices: list[int]) -> str:
    res = []
    ss = list(s)

    for i in range(len(indices)):
        index = indices.index(i)
        res.append(ss[index])

    return ''.join(res)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s, indices))