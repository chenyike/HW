############################################################
# recursion and list comprehension
############################################################

############################################################
# RANDOM START TO CLASS
# google "recursion", below the search box will read: "Did you mean: recursion"
############################################################

############################################################
# some rules of recursion:
# 1. there must be a base case -- termination condition
# 2. the function calls itself with a smaller number each time -- reduction step
############################################################

############################################################
# PART 1: run in the IDLE, takes input argument
############################################################

def main():
    loopnum = int(input("How many times would you like to loop? "))
    counter = 1
    recurr(loopnum, counter)
 
def recurr(loopnum, counter):
    if loopnum > 0:
        print "This is loop iteration:", counter
        recurr(loopnum - 1, counter + 1)
    else:
        print "The loop is complete."
 
main()

############################################################
# PART 2: functions they can all write, but now with recursion
############################################################

# SUMMING A LIST

def iterative_listsum(lst):
    theSum = 0
    for i in lst:
        theSum = theSum + i
    return theSum

print(listsum([1, 3, 5, 7, 9]))

def listsum(lst):
   if len(lst) == 1: # base case
        return lst[0]
   else:
        return lst[0] + listsum(lst[1:]) # reduction step

print(listsum([1, 3, 5, 7, 9]))

############################################################

# FACTORIAL

def iterative_factorial(n):
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result

def factorial(n):
    if n == 1: # base case
        return 1
    else:
        return n * factorial(n - 1) # reduction step

############################################################

# FIBONACCI

def iterative_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib(n):
    if n == 0: # base case
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2) # reduction step

############################################################
# PART 3: list comprehensions
############################################################

lst = [ expression for name in list]

li = [3, 6, 2, 7]
print [ elem * 2 for elem in li ] # [6, 12, 4, 14]

li = [(‘a’, 1), (‘b’, 2), (‘c’, 7)]
print [ n * 3 for (x, n) in li ] # [3, 6, 21]

############################################################

lst = [ expression for name in list if filter]

li = [3, 6, 2, 7, 1, 9]
print [ elem * 2 for elem in li if elem > 4 ] # [12, 14, 18]

############################################################

lst [ expression for name in [expression for name in list] ]

li = [3, 2, 4, 1]
print [elem*2 for elem in [item + 1 for item in li]] # [8, 6, 10, 4]

###############################
lambda expression reduce

f = lambda a,b: a if (a > b) else b 
reduce (f, [47,11,42,102,13])



 
