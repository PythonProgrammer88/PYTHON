
import sys

x = int(sys.argv[1])

if (x < 0):
    print('Invalid Floor')
elif (x == 0):
    print('Ground floor')
elif (x == 1):
    print("1st floor")
elif (x == 2):
    print ("2nd floor")
elif (x == 3):
    print ("3rd floor")
elif (x == 4):
    print ("4th floor")
elif (x == 5):
    print ("5th floor")
else:
    print ('Roof Top reached' )