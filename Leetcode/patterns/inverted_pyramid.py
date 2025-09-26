n = int(input("Input the number of rows you want"))

for i in range(n , 0 ,-1):
    print(" " * (n-i) + "*" * (2*i -1) )

# the logic is same for the straight pyramid only we are counting it from back