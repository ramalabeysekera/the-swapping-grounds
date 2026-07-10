import time
from data import nums


def merge(first: list[int], second: list[int]) -> list[int]:
    i, j = 0, 0
    final = []
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    if i < len(first):
        final.extend(first[i:])
    else:
        final.extend(second[j:])
    return final


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    first_end = len(nums) // 2
    return merge(merge_sort(nums[:first_end]), merge_sort(nums[first_end:]))


start = time.perf_counter()

merge_sort(nums.copy())

end = time.perf_counter()

print(f"Took {end - start:.6f} seconds")
