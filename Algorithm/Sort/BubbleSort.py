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
        print i
        count=0
        for j in range(1,n-i):
            count+=1
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
        print 'count:',count
    print arr


arr=[4324213424,24124112,456,56,25,35235,314,67,9,2134,7,63464,87,65,879,245,46,565,325]

print arr

bubbleSort(arr)