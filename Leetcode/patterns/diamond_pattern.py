# in this pattern we neeed both the inverted and non inverted pyramidn patterns 

n = 5 

for i in range(1 , n-1):
    print(" " * (n-i)  + "*" * (2*i - 1))

# for bottom pyramid 

for i in range( n-1 , 0 , -1):
    print(" " * (n-i) + "*" *(2*i - 1))