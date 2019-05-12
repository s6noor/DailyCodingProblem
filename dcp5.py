# Daily coding problem 4 -- but I mislabeled, so its 5 now
# Source: Stripe
# Given an array of integers, find the first missing positive 
# integer in linear time and constant space. In other words, 
# find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#### First solution: apparently this is O(nlogn + n) time
# 1- I would get rid of the negative numbers
# 2- Then sort the array -- potentially most time consuming part
# 3- then see whats the next expected number
# 4- compare the expected number with the one thats there 
# 5- if its the same then continue
# 6- otherwise return that number

def first_lost(myarray):
    
    #append the value in myarray to newarray if its positive
    newarray = [x for x in myarray if x >= 0]
    newarray = store_sort(newarray)
    for i,num in enumerate(newarray):
        if newarray[i+1] != num+1: return num+1
        else: continue

# This is the simplest form of the sorting algorithm, but it quiet slow
# it will run the loop as many times as the n*(len)

def sort_array(newarray):
    swap = True
    x=-1
    while swap:
        swap = False
        x=x+1       
        for i in range(1,len(newarray)-x):
            if newarray[i] < newarray[i-1]:
                newarray[i], newarray[i-1] = newarray[i-1], newarray[i]
                swap = True
    return newarray

# Lets try sorting in another way: by storing minimum and just moving that around
# this will loop through the array length (array) times, doesnt use too much extra space
def store_sort(newarray):
    for i in range(0, len(newarray)):
        min = newarray[i]
        index=i
        for j in range(i+1,len(newarray)):
            if newarray[j] < min:
                newarray[j], newarray[index] = newarray[index], newarray[j]
                min = newarray[i]
                index = i  
    return newarray

# test sorting
b = [3, 4, -1, 1]
print(store_sort(b))

#test the code itself
#print(first_lost(b))