import time
from data import nums


def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort(nums: list[int], low: int, high: int) -> list[int]:
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)
    return nums


start = time.perf_counter()

quick_sort(nums.copy(), 0, len(nums) - 1)

end = time.perf_counter()

print(f"Took {end - start:.6f} seconds")
