from ast import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + right // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2


solutions = Solution()

print(solutions.search(nums, target))


