#-------------------------------------------------------------------------------
# Name:        duble rect
# Purpose:
#
# Author:      redof
#
# Created:     15-03-2022
# Copyright:   (c) redof 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()

class Rect:
    def __init__(self,x1,y1,x2,y2):

        self.x1=min(x1,x2)
        self.y1=min(y1,y2)
        self.x2=max(x1,x2)
        self.y2=max(y1,y2)

    def check_in( self, x,y):
        if( self.x1<=x and x<= self.x2) and (self.y1<=y and y<=self.y2) :
            return True
        else:
            return False

    def intersection_rect( self, rect ):
        x1 = max(self.x1, rect.x1)
        y1 = max(self.y1, rect.y1)
        x2 = min(self.x2, rect.x2)
        y2 = min(self.y2, rect.y2)

        if( x1 > x2 ) or ( y1 > y2 ):
            print( "Intersection is nothing ")
            return Rect( 0,0,0,0 )
        else:
            print( "Intersection Rect is (%.1f,%.1f), (%.1f,%.1f)" %(x1, y1, x2, y2) )
            return Rect(x1,y1,x2,y2)


    def get_area(self):
        return  ((self.x2 - self.x1)*(self.y2 - self.y1))


    def print(self):
        print( "(%.1f,%.1f), (%.1f,%.1f)" %(self.x1, self.y1, self.x2, self.y2) )

x1,y1,l1 = map(float,[0,0,2])
x2,y2,l2 = map(float,[2,2,2])


rect1 = Rect( x1-(l1/2), y1-(l1/2), x1+(l1/2), y1+(l1+l1/2))
rect2 = Rect( x2-(l2/2), y2-(l2/2), x2+(l2/2), y2+(l2/2))
rect1.print()
rect2.print()


print( rect1.check_in(-1,3))
inter_rect=rect1.intersection_rect(rect2)
inter_rect.print()
print( "Inter Rect Area :: %.2f" %(inter_rect.get_area()))






