'''
Description:
    Given a list of non-overlapping axis-aligned rectangles rects,
    write a function pick which randomly and uniformily picks
    an integer point in the space covered by the rectangles.

    Note:
    An integer point is a point that has integer coordinates.
    A point on the perimeter of a rectangle is included
        in the space covered by the rectangles.
    ith rectangle = rects[i] = [x1,y1,x2,y2],
        where [x1, y1] are the integer coordinates of
        the bottom-left corner, and [x2, y2] are the integer
        coordinates of the top-right corner.
    length and width of each rectangle does not exceed 2000.
    1 <= rects.length <= 100
    pick return a point as an array of integer coordinates [p_x, p_y]
    pick is called at most 10000 times.

    Input:
    ["Solution","pick","pick","pick"]
    [[[1,1,5,5]],[],[],[]]
    Output:
    [null,[4,1],[4,1],[3,3]] '''


# Solution
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = [(x2+1-x1)*(y2+1-y1) for x1, y1,x2,y2 in rects]
        weights_sum = sum(self.weights)
        self.weights = [x/weights_sum for x in self.weights]

    def pick(self):
        x1,y1,x2,y2 = random.choices(
            population=self.rects,
            weights =self.weights,
            k = 1
        )[0]
        x = random.randint(x1,x2)
        y = random.randint(y1,y2)
        return (x,y)




