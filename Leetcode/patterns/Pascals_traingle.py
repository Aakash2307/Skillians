#  no we gonna create pascals traingle here

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

n = 5 

triangle = [[1]]

for i in range(1,n):
    row = [1]
    for j in range(1,i):
        row.append(triangle[i-1][j-1]  + triangle[i-1][j])

    row.append(1)
    triangle.append(row)

for i in range(n):
    print(" "*(n-i), end="")
    print(" ".join(map(str, triangle[i])))