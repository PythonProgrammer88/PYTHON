
import sys

'''
    Module to read a text file and convert each word 
    first letter to CAPS.
    
    Execution of module takes a single argument that is 
    file to read and convert.
'''

def readfile(fileName):
    '''
       Reads input file passed as an agrument process the data
       and prints capitalized words to console.
       Args:
            Takes fileName as an argument
    '''
    try:
        fp = open(fileName, mode='rt', encoding='utf-8')
        words = fp.read().split()
        newWords = convertToCaps(words)
        print('Words in Capitalized form')
        for word in newWords:
            print (word)
        fp.close()
    except Excpetion as error:
        print(error)

def convertToCaps(wordsList):
    '''
       Reads input fila passed as an agrument process the data
       and prints capitalized words to console.
       Args:
            Takes wordsList as an argument
       Returns:
            returns wordsList with capitalized letter in each word
    '''
    capitalizedWords = []
    for word in wordsList:
        capitalizedWords.append(word.capitalize())
    return capitalizedWords

def main(inputfile):
    readfile(inputfile)

if(__name__ == '__main__'):
    if (len(sys.argv) < 2):
        print('Module takes file as input provide a file name:')
        exit (0)
    main(sys.argv[1])
