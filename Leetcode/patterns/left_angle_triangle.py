# Now coding this a left angled triangle

n = int(input(" input the number of rows "))

for i in range(1,n+1):
    #  print the spaces first 

    for j in range( n-i):
        print(" " , end="")


    for k in range(i):
        print("*" , end="")


    print()