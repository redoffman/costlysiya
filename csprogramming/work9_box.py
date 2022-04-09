
class Box :
    def __init__(self, x_start, y_start, z_start, x_end, y_end, z_end) :
        self.x_start = x_start
        self.y_start = y_start
        self.z_start = z_start
        self.x_end = x_end
        self.y_end = y_end
        self.z_end = z_end
    

    def intersection( self, box ):

        x_s = max( self.x_start, box.x_start )
        y_s = max( self.y_start, box.y_start )
        z_s = max( self.z_start, box.z_start)
        x_e = min( self.x_end, box.x_end )
        y_e = min( self.y_end, box.y_end )
        z_e = min( self.z_end, box.z_end )

        return Box( x_s, y_s, z_s, x_e, y_e, z_e )

    def shape( self):
        
        if self.x_start < self.x_end and self.y_start < self.y_end and self.z_start < self.z_end :
            return "VOL"
        elif self.x_start > self.x_end or self.y_start > self.y_end or self.z_start > self.z_end :
            return "NULL"
        elif self.x_start == self.x_end and self.y_start == self.y_end and self.z_start == self.z_end :
            return "POINT"
        elif ( self.x_start == self.x_end and self.y_start == self.y_end )  \
            or ( self.y_start == self.y_end and self.z_start == self.z_end ) \
            or ( self.z_start == self.z_end and self.x_start == self.x_end ) :
            return "LINE"
        elif self.x_start == self.x_end or self.y_start == self.y_end or self.z_start == self.z_end:
            return "FACE"
        else :
            return "NULL"

    def print(self):
        print ( f"Box ({self.x_start}, {self.y_start},{self.z_start})({self.x_end},{self.y_end},{self.z_end})")
test_input=[ "1 3 2 3 8 4   2 5 2 4 6 5 " \
            , "4 3 1 6 6 8   6 5 2 9 7 5" \
            , "5 3 1 9 5 8   1 5 4 5 8 5 "\
            , "3 4 5 7 6 9   7 6 1 8 7 5 "]
test_input2=[ "12 10 18 28 14 27   28 4 2 32 23 26 "\
            , "1 12 8 2 17 23      11 15 5 12 19 6 "\
            , "15 5 5 30 25 9      43 25 15 45 50 46"\
            , "3 3 3 8 8 8         5 5 5 11 11 11 "] 
for i in range(4):
    #points=input().split()
    points=test_input[i].split()
    box1=Box(int(points[0]), int(points[1]), int(points[2]), int(points[3]), int(points[4]), int(points[5]) )
    box2=Box(int(points[6]), int(points[7]), int(points[8]), int(points[9]), int(points[10]), int(points[11]) )
    
    inter_box = box1.intersection(box2)
    inter_box.print()
    print(inter_box.shape())


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')