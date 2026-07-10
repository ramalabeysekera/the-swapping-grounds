nums = [4, 2, 1, 3]


def indent(depth: int) -> str:
    return "  " * depth


def merge(first: list[int], second: list[int], depth: int = 0) -> list[int]:
    pad = indent(depth)
    print(f"{pad}merge({first}, {second})")

    i, j = 0, 0
    final = []

    while i < len(first) and j < len(second):
        print(f"{pad}  compare first[{i}]={first[i]} and second[{j}]={second[j]}")
        if first[i] <= second[j]:
            print(f"{pad}  take {first[i]} from left")
            final.append(first[i])
            i += 1
        else:
            print(f"{pad}  take {second[j]} from right")
            final.append(second[j])
            j += 1

    if i < len(first):
        print(f"{pad}  left over from left: {first[i:]}")
        final.extend(first[i:])
    if j < len(second):
        print(f"{pad}  left over from right: {second[j:]}")
        final.extend(second[j:])

    print(f"{pad}return {final} from merge")
    return final


def merge_sort(arr: list[int], depth: int = 0) -> list[int]:
    pad = indent(depth)
    print(f"{pad}merge_sort({arr})")

    if len(arr) < 2:
        print(f"{pad}base case reached, return {arr}")
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    print(f"{pad}split into {left_part} and {right_part}")

    left_sorted = merge_sort(left_part, depth + 1)
    print(f"{pad}left sorted -> {left_sorted}")

    right_sorted = merge_sort(right_part, depth + 1)
    print(f"{pad}right sorted -> {right_sorted}")

    result = merge(left_sorted, right_sorted, depth + 1)
    print(f"{pad}merge_sort({arr}) returning {result}")

    return result


sorted_nums = merge_sort(nums)

print(f"\nFinal result: {sorted_nums}")
