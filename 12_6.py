import numpy as np


def find_shortest_subarray_1(
        webpage_content: list,  # len=n
        keywords: set,  # len=m
) -> list[int]:
    '''
    O(nm)
    '''
    tracker = {}
    find_all_flag = False
    min_length = np.inf
    min_start = 0
    min_end = 0
    for i in range(len(webpage_content)):
        if webpage_content[i] in keywords:
            keyword = webpage_content[i]
            tracker[keyword] = i
            if (find_all_flag) or (len(tracker.keys()) == len(keywords)):
                find_all_flag = True
                start = min(tracker.values())
                end = max(tracker.values())
                length = end - start + 1
                if length < min_length:
                    min_length = length
                    min_start = start
                    min_end = end
    return [min_start, min_end]

