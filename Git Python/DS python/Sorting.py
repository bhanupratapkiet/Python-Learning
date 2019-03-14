============================
Python - Sorting Algorithms
============================
1. Sorting refers to arranging data in a particular format. 
Sorting algorithm specifies the way to arrange data in a particular order. 
Most common orders are in numerical or lexicographical order.

2. The importance of sorting lies in the fact that data searching can be optimized to a very high level, 
if data is stored in a sorted manner. Sorting is also used to represent data in more readable formats. 
Below we see five such implementations of sorting in python.

1. Bubble Sort
2. Merge Sort
3. Insertion Sort
4. Shell Sort
5. Selection Sort

==============================
==============================
1. Bubble Sort :
==============================
==============================
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array

array = [1,14,12,54,67,28,61,27,34,62]
list1 = bubbleSort(array)
print(list(list1))
#[1, 12, 14, 27, 28, 34, 54, 61, 62, 67]
=====================
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array

array = [1,14,12,54,67,28,61,27,34,62]
list1 = bubbleSort(array)
print(list(list1))
#[67, 62, 61, 54, 34, 28, 27, 14, 12, 1]
========================
def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
				
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
#[17, 20, 26, 31, 44, 54, 55, 77, 93]
==============================
def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j] < alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
				
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
#[93, 77, 55, 54, 44, 31, 26, 20, 17]
=============================













