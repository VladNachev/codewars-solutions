from cmath import sqrt

def is_square(n):    
    if n  < 0 :
        return False
    elif n == 0 : 
        return True
    else: 
       a = sqrt(n)
       if a * a == n:
           return True
       else:
           return False