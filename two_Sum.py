from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_nums = sorted(nums)

        left, right = 0, len(nums) - 1 
        while left < right:
            num1 = sort_nums[left]
            num2 = sort_nums[right]

            res = num1 + num2 
            if res == target:
                index1 = nums.index(num1)
                index2 = nums.index(num2, index1 + 1) if num1 == num2 else nums.index(num2)
                return [index1, index2]
            elif res < target:
                left += 1
            else:
                right -= 1

        return []



nums = input()
nums = [int(num.strip()) for num in nums]
target = int(input('Nhap target:'))

find_target = Solution.twoSum(nums, target)
print(find_target)