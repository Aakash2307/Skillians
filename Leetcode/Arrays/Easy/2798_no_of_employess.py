# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

# The company requires each employee to work for at least target hours.

# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

# Return the integer denoting the number of employees who worked at least target hours.


# approach 
# use a for and an if loop and say if they havent met the target the increase the count 

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):

        n = len(hours)
        count = 0

        for i in range(n):

            if hours[i] >= target :
                count+=1


        return count
