 import random
class Solution:
    def twoSum(self,nums,target):
        hash_table = {}
        out_put = []
        for index , number in enumerate(nums):
            num1 = target - number

            if num1 not in hash_table.keys():
                hash_table[number] = index
                continue

            else:
                val1 = index
                val2 = hash_table.get(num1)
                out_put.append(val1)
                out_put.append(val2)
                return out_put