# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/1.
'''

'''
插入排序算法实现 
'''

def insertSort(arr):

    for j in range(1,len(arr)):

        i=j
        while i>0:
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                i=i-1
            else:
                break

    print arr


arr=[56,25,67,9,2134,7,87,65,879,245]

print arr

insertSort(arr)
