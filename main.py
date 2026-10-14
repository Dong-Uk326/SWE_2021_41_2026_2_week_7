from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
	# Store previously seen numbers and their indices
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
