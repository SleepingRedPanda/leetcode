def merge(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return intervals

    intervals.sort()

    output = [intervals[0]]

    for start, end in intervals[1:]:
        if start > output[-1][1]:
            output.append([start,end])
        elif end > output[-1][1]:
            output[-1][1] = end
    return output

print(merge([[1,3],[2,6],[8,10],[15,18]]))