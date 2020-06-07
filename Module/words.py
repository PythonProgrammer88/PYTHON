
'''
    Module to read a text file and convert each word 
    first letter to CAPS.
'''

def readfile(fileName):
    '''
       Reads input file passed as an agrument process the data
       and prints capitalized words to console.
       Args:
            Takes fileName as an argument
    '''
    fp = open(fileName, mode='rt', encoding='utf-8')
    words = fp.read().split()
    newWords = convertToCaps(words)
    print('Words in Capitalized form')
    for word in newWords:
        print (word)
    fp.close()
    

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