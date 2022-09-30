def mostWordsFound(sentences: list[str]) -> int:
    # res = 0
    # for sent in sentences:
    #     sent = sent.split(' ')
    #     if len(sent)-1 >= res:
    #         res = len(sent)
    # return res

    return max(s.count(" ") for s in sentences) + 1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))