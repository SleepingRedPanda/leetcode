def finalValueAfterOperations(operations: list[str]) -> int:
    # res = 0
    # for operation in operations:
    #     if '++' in operation:
    #         res += 1
    #     elif '--' in operation:
    #         res -= 1
    # return res

    o_dict = {'+': 1, '-': -1}
    return sum(o_dict[op[1]]for op in operations)