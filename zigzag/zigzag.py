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

def check(array):
    print 'array is ', array
    for i in range(len(array)-1):
        if i % 2 == 0 and array[i] > array[i+1]:
            return False
        if i % 2 == 1  and array[i] < array[i+1]:
            return False
        
        return True
    
from random import randint

x=[randint(0,9) for p in range(randint(0,9))]
    
print (check(zigzagArray(x)))