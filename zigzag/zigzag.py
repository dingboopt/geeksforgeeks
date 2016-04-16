'''
Created on 2016 4 16

@author: Administrator
'''
def zigzagArray(array):
    for i in range(len(array)-1):
        if i % 2 == 0 and array[i] > array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp
        if i % 2 == 1  and array[i] < array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp 
    return array

print (zigzagArray([3,5,2,1,7,9]))