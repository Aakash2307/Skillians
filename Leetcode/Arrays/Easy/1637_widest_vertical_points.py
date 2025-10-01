# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.



# key idea 
# retrieve the coordinates of x 
# sort the x coordinates

# find the max gap by setting initially set to 0 and find the difference and between x and its previous x coordinates 

#  retrive the result 

class Solution(object):
    def maxWidthOfVerticalArea(self, points):

        # first retirive the x coordinates 

        xs = [x for x , y in points]

        xs.sort()

        max_gap = 0

        for i in range(1 , len(xs)):
            max_gap = max(max_gap , xs[i] - xs[i-1])

        return max_gap



