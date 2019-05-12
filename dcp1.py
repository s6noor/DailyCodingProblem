# Daily coding problem 1
# Source: Google
# Problem: Given a list of numbers and a number k, return whether any two numbers
# from the list add up to k
# Problem Solution should look like:
#       Given array = [10,15,3,7] and k = 17
#       return true since 10+7 = 17
##################################################################################
# Different ways of solving this
# One way to do this is to go through each number and check the addition of each one
# if we do this, for an array of size n, there will be n^2 computations
def sumall(array,k):
    copy = array
    for i in array:
        for j in copy:
            sum = i + j
            if sum == k: return True
            else: continue

# Good but not good enough
# Lets see how else I can do this
# Another way to do this is take the array, start from the first term n, see if the 
# difference of the actual number and nth number is in the remaining 
# array. If so, return true, otherwise return false
# In this method, the computation is performed n times 

# A potential bug in this would be what if the remaining result is equal to the number in i itself, that would be
# doubling the result and hence incorrect. So, lets take that away...

def justcheck(array,k):
    for i in range(0,len(array)):
        #calculate difference
        remaining = k-array[i]
        #make a copy of the array and remove the number at the index i (dont want to remove the number cause it may occur multiple times)
        checkarray = array.copy()
        checkarray.pop(i)
        if remaining in checkarray: return True
        else: continue

coolstuff = [10,7,3,7]
print(sumall(coolstuff,14))

print(justcheck(coolstuff,21))