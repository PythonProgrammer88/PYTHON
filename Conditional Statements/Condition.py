
import sys
'''
    Program to demonstrate conditional statements in python
    Conditional statements in python if else
'''

def BookTickets():
    '''
        Reads Seating  Capacity and ticket Count as command
        line arguments.
        Using if and else condition to control the program flow
    '''
    try:
        SeatingCapacity = int(sys.argv[1])
        TicketCount = int(sys.argv[2])
        if ((SeatingCapacity - TicketCount) > 0 ):
            print('Seats Available for Booking.. ', SeatingCapacity)
        else:
            print('No More Booking Allowed')
        
    except Exception as error:
        print(error)
    

if (len(sys.argv) < 3):
    print('Program Takes 2 arguments Seating Capacity and Ticket Count')
    exit(0)

BookTickets()
