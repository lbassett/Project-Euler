import math

def is_prime(n):
    if type(n) != type(3):
        return(False)
    elif n<=1:
        return(False)
    elif n <= 3:
        return(True)
    else:
        if (n % 2 == 0) or (n %3 == 0):
            return(False)
        else:
            squareroot = math.sqrt(n)
            x = 5
            while x<squareroot:
                if (n % x == 0) or (n % (x+2) == 0):
                    return(False)
                x += 6
            return(True)

for x in range(100):
    print(x, is_prime(x))
        

    
