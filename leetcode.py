# -*- coding:utf-8 -*-
from utils.data_structure import *

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

'''
Issue: #0002
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.abs
Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

source: LeetCode
link: https://leetcode-cn.com/problems/add-two-numbers
'''
class solution_0002(object):
    def add_two_numbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        carry = 0
        node = ListNode(0)
        curr = node
        while l1 is not None or l2 is not None:
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            z = x + y + carry
            curr.next = ListNode(z % 10)
            curr = curr.next
            if z / 10 >= 1:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            curr.next = ListNode(carry)
        return node.next

'''
Issue: #0004
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5

source: leetcode
link: https://leetcode-cn.com/problems/median-of-two-sorted-arrays
'''
class solution_0004(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        '''
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        '''
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l % 2 == 1:
            return nums[l/2]
        else:
            left = nums[l/2 - 1]
            right = nums[l/2]
            return (left + right) / 2.0

if __name__ == "__main__":
    pass
