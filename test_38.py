#!/usr/bin/python3
list = []
while True:
    nums = int(input())
    if (nums==42):
        for number in list:
            print(number)
        while(1):
            nums = input()
    list.append(nums)