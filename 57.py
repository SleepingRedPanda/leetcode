def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    output = []

    for i, (start, end) in enumerate(intervals):
        if end < newInterval[0]:
            output.append()

intervals = [[1,3],[6,9]]
newInterval = [2,5]

print(insert(intervals, newInterval))