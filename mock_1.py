""" Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

Note: Create a GitHub file for the solution and add the file link the the answer section below.

5 points
"""
def solve_problem(array):
    new_array = list()
    count = 0
    if len(array) < 1: 
        return 0
    for i in array:
        if i == 0: 
            count += 1
        else:
            new_array.append(i)
    for i in range(count):
        new_array.append(0)
    print(new_array)
    return new_array

print(solve_problem([0, 1, 0, 3, 12]))

"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.

Note: Create a GitHub file for the solution and add the file link the the answer section below.
"""
def solve_problem(string):
    for i in range(len(string)): 
        if string.count(string[i]) == 1:
            print(string[i], i)
            return i
    return -1
        
        
print(solve_problem('aabb'))
            
