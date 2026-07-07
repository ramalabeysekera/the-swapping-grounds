from data import nums
import time


def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j: int = i
        while j > 0 and (nums[j - 1] > nums[j]):
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


start = time.time()

insertion_sort(nums.copy())

end = time.time()

print(f"Took {end - start:.6f} seconds")
