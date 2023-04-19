# __*__coding: utf-8
# @Time : 2023/4/19 
# @ Author :lvlongxin
# @File : The_sum_of_the_three_numbers
# @Prooject : algorithm_my
# 三数之和
# 给定一个数组，找出三个元素，使他们相加等于一个数，，所有满足条件的不重复的三元组

# 不要求返回下标，所以优先进行排序
from typing import List
class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while(l < r):
                if (nums[i] + nums[l] + nums[r] < target):
                    l += 1
                elif (nums[i] + nums[l] + nums[r] > target):
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while(l < r and nums[l] == nums[l + 1]):
                        l += 1
                    while(l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    tmp = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    pp = tmp.threeSum(nums, target)
    print(pp)

