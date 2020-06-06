
'''
    Module to read and write files
    Demonstrates how to read and write files
'''

def readfile(fileName):
    '''
        Reads the given input file and prints data to 
        console using python read function
        Args:
            Takes file name as a argument
    '''
    fp = open(fileName, mode='rt', encoding='utf-8')
    # Read complete file to list
    print("Reading File to a List and print line by line: \n")
    dataList = fp.readlines()
    for line in dataList:
        print(line)
    
    fp.seek(0) # Reset the file pointer to the beginning of file
    
    # Reading file line by line using loop
    print("Reading File Line by Line: \n")
    newLine = fp.readline()
    while(newLine):
        print(newLine)
        newLine = fp.readline()
        
    fp.close()

def writefile(fileName):
    '''
        Opens the file in write mode and writes text data 
        to the file.
        Args:
            Takes file name as a argument
    '''
    fp = open(fileName, mode='wt', encoding='utf-8')
    fp.write('Programming helps to automate the process of manual work.')
    fp.write('Automation makes work less error prone \n')
    fp.write('Practice Programming')
    
    # To write data from list to file use writelines function of python
    
    fp.close()