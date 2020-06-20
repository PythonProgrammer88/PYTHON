import sys

'''
    Program to demonstrate while loop 
    Reads a string and prints each word.    
'''
def printWords(string):
    '''
        print Words function reads the strings, splits on space
        loops through the words and prints the words
        
        Args:
            Takes a string as a input
        Returns:
            no return
    '''
    wordList = string.split()
    for word in wordList :
        print(word)
        

if (__name__ == '__main__'):
    if(len(sys.argv) < 2):
        print('Provide string as an argument')
        exit(0)
    inpStr = sys.argv[1]
    printWords(inpStr)