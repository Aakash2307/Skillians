# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.



# for this I made an approach where I could just store a value this was my main problem then found a counter type var called x
# here in x I would store the value based upon the operations  



class Solution(object):
    def finalValueAfterOperations(self, operations):

        n = len(operations)

        x = 0

        for i in operations:
            if i == "X++" or i == "++X":
                x+=1
            elif i == "--X" or i== "X--":
                x-=1

            
        return x 