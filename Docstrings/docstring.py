"""
   Reads a number and returns even or odd
   
    Usage:
        python docstrings.py <number>
"""

import sys

def even_or_odd(n):
    """
        Evaluates if a passed number is even or odd
        
    Args:
        Takes one argument as number
    Return:
        returns the result even or odd
    """
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")

def main(x):
    """Calls even_or_odd function passing the argument
    """
    even_or_odd(x)
    
if "__name__" == "__main__":
    main(sys.argv[1])