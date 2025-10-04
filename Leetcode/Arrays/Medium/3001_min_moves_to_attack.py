#  this is a mid level quesition which I was not able to solve a bit so I didnt found any approach to solve this so I went 
# chatgpt 

class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        # Rook can attack if same row or column
        if a == e or b == f:
            # Check if bishop is blocking rook’s path
            if (a == e and a == c) and ((d - b) * (d - f) < 0):
                return 2
            if (b == f and b == d) and ((c - a) * (c - e) < 0):
                return 2
            return 1

        # Bishop can attack if they are on same diagonal
        if abs(c - e) == abs(d - f):
            # Check if rook is blocking bishop’s path
            if abs(c - a) == abs(d - b) and abs(e - a) == abs(f - b) and ((b - f) * (b - d) < 0):
                return 2
            return 1

        # Otherwise, needs 2 moves
        return 2
