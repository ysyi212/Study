#!/root/ysy/python/bin/python3
'''qsort
quick sort
'''
from random import randint

def q_sort(nums):
    if len(nums) < 2:
        return nums

    middle = nums[0]
    smaller = []
    larger = []

    for data in nums[1:]:
        if data < middle:
            smaller.append(data)
        else:
            larger.append(data)

    return q_sort(smaller) + [middle] + q_sort(larger)

if __name__ == '__main__':
    nums = [randint(0, 100) for i in range(10)]
    print(nums)
    print(q_sort(nums))