# given a String s consist of 0s and 1s only. You are allowed to pick atmost one substring from it and convert every 0 to 1 and every 1 to 0 in that substring. Print the maximum number of 1s we can achieve.



# input = 1100010 , ans= 6



# O(N) solution:



s = "10101011"

n=len(s)

maxProfit=0

intialOnes = 0

count=0

for char in s:

    if char=="1":

        intialOnes = intialOnes+1

for char in s:

    if char=='1':

        count=count-1

    else:

        count=count+1

    if count<0:

        count=0

    maxProfit=max(maxProfit,count)

print(maxProfit+ intialOnes)



# O(n^3):

        



for i in range(0,n):

    for j in range(i,n):

        # every pair of index i,j where (j>=i)

        count = 0

        substr=""

        for k in range(i,j+1):

            substr=substr+s[k]

            if s[k]=='0':

                count=count+1

            else:

                count=count-1

        print(substr)

        maxProfit = max(maxProfit,count)

print(maxProfit+intialOnes)