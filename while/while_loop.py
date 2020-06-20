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
    wordCount = len(wordList)
    k = 0
    while(k < wordCount):
        print(wordList[k])
        k += 1
        
        

if (__name__ == '__main__'):
    if(len(sys.argv) < 2):
        print('Provide string as an argument')
        exit(0)
    inpStr = sys.argv[1]
    printWords(inpStr)