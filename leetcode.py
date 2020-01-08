# -*- coding:utf-8 -*-

'''
Issue: #0001
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

source: LeetCode
link: https://leetcode-cn.com/problems/two-sum
'''
class solution_0001(object):
    def two_sum(self, nums, target):
        '''
        Args: 
            nums: List[int]
            target: int
        Returns:
            List[int]
        '''
        nums_sort = sorted(nums)
        for i, n in enumerate(nums_sort):
            complement = target - n
            nums_slice = nums_sort[i + 1:]
            if complement <= nums_slice[-1] and complement >= nums_slice[0]:
                if complement in nums_slice:
                    if complement == n:
                        index1 = nums.index(n)
                        nums.pop(index1)
                        index2 = nums.index(n) + 1
                        return index1, index2
                    else:
                        return nums.index(n), nums.index(complement)
        return None
