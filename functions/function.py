'''
    Module to demonstrate functions
    Dclaring and Defining functions
    
    Functions in python are defined using the 'def' keyword followed by function name 
    and arguments to the function and a colon to start a new block.
    
    def functionName(arguments):
'''

def square(x):
    '''
        Square function evaluates square of passed argument
        Args:
            Takes a single Argument number as input
        Return:
            Returns square of a number
    '''
    return x*x
    
def odd_or_even(n):
    '''
        odd_or_even function evaluates passed argument is odd or even
        Args:
            Takes a single Argument number as input
        Return:
            Returns string even or odd
    '''
    if (n%2 == 0):
        print("even")
        return
    else:
        print("odd")
        
        