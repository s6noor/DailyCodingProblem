# Given a list of integers, write a function that returns the largest sum of 
# non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we 
# pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def adj_sum(arr):
    currsum = [0 for i in range (0,3)]

    #make an array to keep track of sums for non adjacents and initialize some numbers
    currsum[0] = arr[0]
    currsum[1] = max(arr[0],arr[1])

    #now, start from the 2nd number and compare.
    for i in range(2,len(arr)):

        #the next sum array is the max number between:
        #       The current nummber plus accumalative of the last non-adjacent numbers
        #       The previous sum

        #since I've initialized in the beginning, best to compare the initial value seperately because I need to include the 0th term
        if i ==2: currsum[2] = max(arr[i] + currsum[0],currsum[1])
        else:
            temp = currsum[2]
            currsum[2] = max(arr[i] + currsum[1],temp)
            currsum[0] = currsum[1]
            currsum[1] = temp
    
    #last number of this array is the answer
    return currsum[2]

#accept an input string and convert to int type
arr= input('Enter your array with spaces between numbers and ill tell you the largest sum from that array for non-adjacent numbers: ')
arr = list(map(int,arr.split()))
print('Your largest sum is: ',adj_sum(arr))

#### Justification for the constant space
# I used an array of length 3 for keeping track of my maximums for the previous
# no matter what the length of the array, I will only use a space of 3

#### Justification for linear time
# Im doing this as im passing through the array. The amount of time taken for this
# is directly proportional to the length of the given array. 