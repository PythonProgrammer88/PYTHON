'''
    Module demonstrates exception Handling
'''

def ConvertToInteger(x):
    ''' ConvertToInteger function 
        Converts passed argument to Integer
        Args:
            Takes an argument and converts to Integer
        Return:
            Returns an integer number.
            In case of Exception error code -1 is returned
    '''

    try:
        num = int(x)
    except:
        errCode = -1
        return errCode
    return num
    

def CountWordsInfile(file):
    ''' CountWordsInfile function 
        Counts the total number of words in file
        Args:
            Takes a single argument fileName 
        Return:
            Return the number of words in the file
    '''

    try:
        fp = open(file, mode='rt', encoding='utf-8')
        data = fp.read()
        words = data.split()
        fp.close()
        print ("words in text file: ",len(words))
        return len(words)
    except Exception as error:
        print("Exception Occured and Exception is:")
        print(error)