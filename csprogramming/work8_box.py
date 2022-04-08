
class Rect :
    def __init__(self, x_start, y_start, x_end, y_end) :
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
    

    def intersection( self, rect ):

        x_s = max( self.x_start, rect.x_start )
        y_s = max( self.y_start, rect.y_start )
        x_e = min( self.x_end, rect.x_end )
        y_e = min( self.y_end, rect.y_end )

        return Rect( x_s, y_s, x_e, y_e )

    def shape( self):
        
        if self.x_start < self.x_end and self.y_start < self.y_end :
            return "FACE"
        elif self.x_start == self.x_end and self.y_start == self.y_end :
            return "POINT"
        elif self.x_start == self.x_end or self.y_start == self.y_end :
            return "LINE"
        else :
            return "NULL"

    def print(self):
        print ( f"Rect ({self.x_start}, {self.y_start})({self.x_end},{self.y_end})")
            
for _ in range(4):
    points=input().split()
    rect1=Rect(int(points[0]), int(points[1]), int(points[2]), int(points[3]) )
    rect2=Rect(int(points[4]), int(points[5]), int(points[6]), int(points[7]) )
    inter_rect = rect1.intersection(rect2)
    inter_rect.print()
    print(inter_rect.shape())