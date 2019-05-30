"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def  ReverseInteger(n):
    rev = 0
    if n > 0:
        flag = 1
    else:
        flag = -1
    x = str(abs(n))
    rev = int(x[::-1])
    if rev <= 2 ** 31 - 1:
        return flag * rev
    else:
        return 0


num = int(input("Enter the Signed number to be reversed: "))
reverse = ReverseInteger(num)
print(reverse)
