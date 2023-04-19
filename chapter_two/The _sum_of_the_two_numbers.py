# __*__coding: utf-8
# @Time : 2023/4/19 
# @ Author :lvlongxin
# @File : The _sum_of_the_two_numbers
# @Prooject : algorithm_my
# 两数之和
# 提供一个数组，数组内两个值的和等于给出的目标值，，返回两个元素的下标
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List [int]:
        n = len(nums)
        nums.sort()         # 重点是排序
        l = 0               # 首下标
        r = len(nums) - 1   # 尾下标
        while (l < r):
            if (nums[l] + nums[r] < target):
                l += 1
            elif (nums[l] + nums[r] > target):    # 最大值和最小值相加，大于的话，，最大值和谁相加都会大于
                r -= 1                            # 最大值左移动，变小
            else:
                return [l, r]
        return []
    # 上面的解法是错的，因为排序会改变数组的索引，，，如果还是想用排序解决的话，需要将索引值作为二维信息保存

    def realTwoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapper = {}
        for i in range(n):
            if (target - nums[i] in mapper):    # 借助一张哈希表，判断是否在之前遇到过，是，直接返回（实际观察，是在key中寻找）
                return [mapper[target - nums[i]], i]
            else:                                # 不是，放入哈希表中
                mapper[nums[i]] = i
        return []




if __name__ == "__main__":
    tmp = Solution()
    number = [2, 4, 12, 13, 7, 11, 15]
    target = 13
    # ll = tmp.twoSum(number, target)
    # print(ll)
    pp = tmp.realTwoSum(number, target)    # 不注释掉上面的代码，进入函数的是一个排好序的数组  sort效果真强
    print(pp)