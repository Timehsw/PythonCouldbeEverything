# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/1.
'''

'''
选择排序算法实现
'''


def selectSort(arr):
    n=len(arr)
    for j in range(n-1):
        min=j
        for i in range(j+1,n):
            if arr[min]>arr[i]:
                min=i
        arr[j],arr[min]=arr[min],arr[j]

    print arr

arr=[56,25,67,9,2134,7,87,65,879,245]

print arr

selectSort(arr)