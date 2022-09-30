def merge(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return [intervals[0]]

    intervals = sorted(intervals, key = lambda x: x[0])

    merged_intervals = [intervals[0]]
    for n, interval in enumerate(intervals[1:]):
        if merged_intervals[-1][1] >= interval[0]:
            merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
        else:
            merged_intervals.append(interval)

    return merged_intervals

print(merge([[1,3],[2,6],[8,10],[15,18]]))