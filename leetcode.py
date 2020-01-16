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

'''
Issue: #1309
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.abs
 

Example 1:

    Input: s = "10#11#12"
    Output: "b"
    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
    Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"

source: leetcode
link: https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping
'''
class solution_1309(object):
    def freq_alphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        FLAG = 0
        TAG = 96
        r_s = str()
        l = len(s)
        for i, s_i in enumerate(s):
            if FLAG == 0:
                if i < l - 2:
                    if s[i+2] == '#':
                        num = eval(s[i:i+2])
                        FLAG = 2
                    else:
                        num = eval(s_i)
                else:
                    num = eval(s_i)
                char = chr(num + TAG)
                r_s += char
            else:
                FLAG -= 1
        return r_s

'''
Issue: #0392

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

source: leetcode
link: https://leetcode-cn.com/problems/is-subsequence
'''
class solution_0392(object):
    def is_subsequence(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        for s_i in s:
            if s_i in t:
                i = t.index(s_i)
                t = t[i + 1:]
            else:
                return False
        return True

'''
Issue: #0009
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

source: leetcode
link: https://dev.lingkou.xyz/problems/palindrome-number
'''
class solution_0009(object):
    def is_palindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
	if x < 0:
            return False
        else:
            s = str(x)
            n = len(s) / 2
            for i in range(n):
                if s[i] != s[-(i + 1)]:
                    return False
            return True

if __name__ == "__main__":
    pass
