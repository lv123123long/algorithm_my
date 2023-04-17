# __*__coding: utf-8
# @Time : 2023/4/17 
# @ Author :lvlongxin
# @File : polynomial
# @Prooject : algorithm_my
from typing import List
class Lvlongxin:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapper = {}
        for i in range(n):
            if target - nums[i] in mapper:
                return (mapper[target -nums[i]], i)

            else:
                mapper[nums[i]] = i
        return []

if __name__ == "__main__":
    tmp = [1, 2, 3, 4, 5]
    ll = 3
    ss = Lvlongxin()
    nn = ss.twoSum(tmp,ll)
    print(nn)