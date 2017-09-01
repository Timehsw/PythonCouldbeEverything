# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/1.
'''

'''
冒泡排序算法实现
'''


def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(1,n-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    print arr


arr=[56,25,67,9,2134,7,87,65,879,245]

print arr

bubbleSort(arr)