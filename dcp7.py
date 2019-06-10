# This has three challenges: Fizz Buzz and Palindrome Challenges
###############################################################################
# 1: Fizz Buzz Challenge
# Print 1 to 100
# if the number is divisible by 3, print fizz
# if the number is divisible by 5, print buzz
# if the number is divisible by 3 and 5 print fizzbuzz

def fizzbuzz():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else: print(i)

##########################################################################
# 2: Palindrome Challenge
# Check if a word is a palindrome (same word if spelt backwards)

def pali_chali(word):
    newword = ''
    for letter in word:
        newword =  letter + newword
    # Can also just use reverse splicing newword = word[::-1]
    print(newword)
    if newword == word:
        print("This is a Palindrome word")
    else: print("Nope, not a Palindrome. Note, this is case sensitive")

#c = 'Dad'
#pali_chali(c)

#######################################################################
# 3: Anagram Challenge
# Check if two words are anagrams of each other
# In this code, I generate a word frequency dictionary from the first word
# then compare it with the second word (by subtracting the frequencies at each encounter)
# if at any point it fails, you return false, other wise keep going and return true

def anag(s,t):
    mydict = dict()
    #right off the bat, if they aint equal in size, they aint anagrams
    if len(s) != len(t): return False
    #now go through first word and build frequency dictionary
    for letter in s:
        #if its in the dictionary already, add to its value
        if letter in mydict:
            mydict[letter] = mydict[letter] +  1
        #if it is not in the dictionary, initialize
        else: 
            mydict[letter] = 1
            continue
    # now go through second word, but use same dictionary as above
    for letter in t:
        # if a particular letter is not in the dictionary, it definately means not anagram
        if letter not in mydict:
            return False
        # if its there, then remove one from the frequency, this is done so that 
        # if you go to a negative number, then you know that a particular letter
        # occured more often than it did in the first word, hence - not an anagram either
        else: mydict[letter] = mydict[letter] - 1
        if mydict[letter] <0: return False
    #if you have passed all that, you rock!
    return True

w1 = input("Enter the first word: ")
w2 = input("Enter the second word: ")
if anag(w1,w2) is True: print("These two are anagrams")
else: print("Nope, not anagrams")
