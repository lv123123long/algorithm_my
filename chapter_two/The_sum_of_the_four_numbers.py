# __*__coding: utf-8
# @Time : 2023/4/20 
# @ Author :lvlongxin
# @File : The_sum_of_the_four_numbers
# @Prooject : algorithm_my
# 四数之和
# 一个数组中，是否包含四个数相加等于一个数的情况，列出所有可能性，并且不重复的四元数组

from typing import List

# 暴力法
class SolutionBaoli:
    def backtrack(self, res: List[List[int]], nums: List[int], n: int, tempList: List[int], remain: int, start: int, hashmap: dict):
        if (len(tempList) > 4):
            return
        if (remain == 0 and len(tempList) == 4):
            if (str(tempList) in hashmap):
                return
            else:
                hashmap[str(tempList)] == True
                return res.append(tempList.copy())

        for i in range(start, n):
            tempList.append(nums[i])
            self.backtrack(res, nums, n, tempList, remain - nums[i], i + 1, hashmap)
            tempList.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        hashmap = {}
        nums.sort()
        self.backtrack(res, nums, len(nums), [], target, 0, hashmap)
        return res

# 分治法
class SolutionFenzhi:
    def fourSum(self, nums: List[int], target: int):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results
    def findNsum(self, nums: List[int], target: int, N: int, tempList: List[int], results: List[int]):
        if len(nums) < N or N < 2:
            return
        if N == 2:
            l =0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(tempList + [nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)):
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, tempList + [nums[i]], results)
        return






if __name__ == "__main__":
    print("pp")
    numbers = [1, 0, -1, 0, 2, -2]
    target = 0

