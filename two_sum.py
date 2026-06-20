#1. Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


#My Solution
target = 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(numbers)):
    next_number = i + 1

    while next_number < len(numbers):

        if numbers[i] + numbers[next_number] == target:
            print([i, next_number])
            break

        next_number += 1