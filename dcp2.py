# Daily coding problem 2
# Source: Uber
# Given an array of integers, return a new array such that each element at index i of the new array is the 
# product of all the numbers in the original array except the one at i
# for example, if input is [1,2,3,4,5] the expected output is [120,60,40,30,24]

###########################################################################################################

# My general approach to solving this problem would be to go through each number, make a copy of the array
# with every number except the index that im at, and then multiply it
# This is good, but I think that it will be memory intensive for a larger array
def calculate_multiple(array):
    new_array = list()
    for i in range(0,len(array)):
        coolarray = array.copy()
        coolarray.pop(i)
        new_array.append(multiply_arrayvals(coolarray)) 
    return new_array

def multiply_arrayvals(array):
    result = 1
    for i in array:
        result = result*i
    return result


# That works. But, lets do this in an easier way. 
# So I know that if I just multiply all the numbers in the array first
# then just divide the ith term, that will give me the answer too

def div(array):
    #first find the multiple of all values
    product = multiply_arrayvals(array)
    new_array = list()
    for i in array:
        new_array.append(product/i)
    return new_array

# Testing....
waddup = [1,2,3,4,5]
print(calculate_multiple(waddup))
print(div(waddup))