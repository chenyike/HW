def isPrime(x):
    '''function that returns whether or not the given number x is prime. This function returns boolean.'''
    n=0
    for i in range(1,x+1):
        if x % i == 0:
            n+=1
    if n==2:
        return True
    else:
        return False
            
def isComposite(x):
    '''function that returns whether or not the given number x is composite. '''
    if isPrime(x)==True:
        return False
    else:
        return True
    
def isPerfect(x):
    '''code that returns whether or not the given number x is perfect. '''
    sum=0
    for i in range(1,x):
        if x % i == 0:
            sum+=i
    if sum==x:
        return True
    else:
        return False

def isAbundant(x):
    '''code that returns whether or not the given number x is abundant. '''
    if isPerfect(x)==True:
        return False
    else:
        return True

def isTriangular(x):
    '''code that returns whether or not the given number x is triangular. '''
    n=0
    for i in range(1,x):
        if x==i*(i+1)/2:
            n+=1
    if n>0:
        return True
    else:
        return False
        
def isPentagonal(x):
    '''code that returns whether or not the given number x is Pentagonal. '''
    n=0
    for i in range(1,x):
        if x==i*(3*i-1)/2:
            n+=1
    if n>0:
        return True
    else:
        return False

def isHexagonal(x):
    '''code that returns whether or not the given number x is Hexagonal. '''
    n=0
    for i in range(1,x):
        if x==2*i*i-i:
            n+=1
    if n>0:
        return True
    else:
        return False

def main():
    while True:
        number=raw_input('Please input an integer between 1 and 1000, input \'-1\' if you want to quit\n')
        number=float(number)            #need to convert string to a number
        while number%1!=0:                  #eliminate the scenario where non-integer exists
            print('Please input an integer!')
            number=input('Please input an integer between 1 and 1000, input \'-1\' if you want to quit\n')
        number=int(number)              #convert float to int
        if number==0 or number<-1 or number>1000:       #ask user to reinput if the previous input was out of range
            print('Out of range!')
            number=input('Please input an integer between 1 and 1000, input \'-1\' if you want to quit\n')
        if number==-1:
            break
        if number>=1 and number<=1000:     #judge which category this number fits
            if isPrime(number):
                Prime=''
            else:
                Prime='not'

            if isComposite(number):
                Composite=''
            else:
                Composite='not'

            if isPerfect(number):
                Perfect=''
            else:
                Perfect='not'

            if isAbundant(number):
                Abundant=''
            else:
                Abundant='not'

            if isTriangular(number):
                Triangular=''
            else:
                Triangular='not'

            if isPentagonal(number):
                Pentagonal=''
            else:
                Pentagonal='not'

            if isHexagonal(number):
                Hexagonal=''
            else:
                Hexagonal='not'

            #final output
            print number, 'is', Prime,'prime, is', Composite,'composite, is', Perfect, 'perfect, is',Abundant, 'abundant, is', Triangular, 'triangular, is', Pentagonal,'pentagonal, is',Hexagonal,'hexagonal.\n'

if __name__== "__main__":
    main()
        
    
        
