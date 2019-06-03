#Daily Coding Problem 8
#Source: Facebook.
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

# So basically, in order to calculate 111 we need to calculate 11 and then in order to calculate 11 we need 1. 
# there will be two ways to decode: decode each letter or decode two letters together
# a combination of these two types of decoding together will help us count a list of all posibilities
# This method solves in O(n) time

def tryme(data,mycache):

    #if end of string, return 1 as there is only one possible way a single number can be decoded
    if len(data) <=0:
        return 1
    
    #if the data is only one number long, then it can obviously only be decoded in one way
    if len(data) == 1:
        return 1
    
    #if there is a 0 in the data, return a 0. There is no letter mapping to 0
    if data[0] == '0':
        return 0
    
    #check if the next node of data has already been counted before: Memoization step
    if int(data[1:]) in mycache: 
        return mycache[int(data[1:])]
   
    #count the number of ways the remaining string can be decoded. So for 111, how many ways can 11 be decoded etc..
    count = tryme(data[1:],mycache)

    #if the length of the data is greater than two, then we need to consider the double digit values too
    #so, if its between 1 and 26, consider that as one possibility too and look at remaining. so for 111 look at count(1) + count(11)
    if len(data) >=2 & int(data[0:1]) <= 26:
        count = count + tryme(data[2:],mycache)
    
    #store these counts in the dictionary for cache
    mycache[int(data[1:])] = count
    
    return count

def call_func():
    mycache = {}
    data = input("Enter a string of numbers: ")
    print(tryme(data,mycache))

call_func()