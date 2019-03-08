# ack.py
# Raunak Anand
# Ackermann Mathematical Function
#

def A(m,n): # defining Ackermann Mathematical Function
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1,1)
    else:
        return A(m-1,A(m,n-1))

# looping the function
while True:

    try: # user input should be an integer
        integer1 = int(input("Please enter a nonnegative integer: "))
        integer2 = int(input("Please enter a nonnegative integer: ")) 

        if int(integer2) <= 0: # user input has to be a nonnegative integer
            print("Please enter a nonnegative integer!")
        elif int(integer1) <= 0: # user input has to be a nonnegative integer
            print("Please enter a nonnegative integer!")
        else:
             print(A(integer1,integer2))

    except ValueError as msg: # user did not enter an integer
        print(msg, "-- please enter a nonnegative integer!")

    except RecursionError as msg: # user inputted too big values
        print(msg, "-- number is too big!")

    except EOFError: # if user wants to quit then help them
        break
        
    
        

        



