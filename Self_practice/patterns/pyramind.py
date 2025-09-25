n = int(input("Input the number of rows you want"))

for i in range(0,n):
    print(" " * (n-i) + "*" * (2*i -1) )


# logic 

# when n = 5 is entered then first space which is n-i which means on first row 5-1 = 4 spaces created and 2*i-1 which is i = 1  will
# be 1 which means one start is being created 
# this way the logic is being created  