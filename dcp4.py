# Daily Coding Problem 4
# Source: Jane Street
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# This definition is called a closure. It lets us define the initial variables and then use
# them as functions later on. So, the enclosing function is cons(), this will need to be defined
# first. This will return a function called pair. now, we can use the variable defined with 
# cons() as a function itself. so b() is a function that will take a function and pass the 
# pair a and b to it. So, if we run b(print) it will print the pair, if we do b(add) it will add the 
# pair

#Good to know here is that the function pair() will have access to all local variables in the 
# cons() as well. This helps making the speed faster, if needed.

## For understanding 
#def car(a,b):
#    print(a)

#def cdr(a,b):
#    print(b)

#b = cons(4,5)
#b(car)
#b(cdr)

#### now this above gives me the results as i desire as well. But the issue here is that
# I have to create that temporary variable b and then pass the defined functions car
# and cdr. What if I wanted to pass the function cons(4,5) into car and cdr? In this case,
# the car and cdr function have to accept a single input of pair type. 
# once it accepts that pair type, it returns the function pair(init_val) which then goes back
# to the initial declaration, calls the pair function which passes init_val(a,b)
# which in turn returns a. 

def car(pair):
    def init_val(a,b):
        return a
    return pair(init_val)

def cdr(pair):
    def last(a,b):
        return b
    return pair(last)

print(car(cons(4,5)))
print(cdr(cons(3,5)))
