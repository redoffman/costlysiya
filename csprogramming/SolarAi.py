#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      redof
#
# Created:     24-03-2022
# Copyright:   (c) redof 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x_size, y_size = map(int, input().split())

matrix= [[0 for col in range(y_size+2)] for row in range(x_size+2)]

def print_matrix():
    global x_size
    global y_size
    global matrix

    for y in range(y_size+2):
        for x in range( x_size + 2 ):
           print( "%2d" %matrix[y][x], end=" ")
        print("")


for i in range(x_size+2):
    matrix[i][0]=-1
    matrix[i][y_size+1]=-1

for j in range( y_size+2):
    matrix[0][j]=-1
    matrix[x_size+1][j]=-1


class Point:
    def __init__(self, x_size, y_size ):
        self.x = 0
        self.y = 0
        self.direction = ""
        self.cell_count=0

        self.matrix= [[0 for col in range(y_size+2)] for row in range(x_size+2)]

        for i in range(x_size+2):
            self.matrix[i][0]=-1
            self.matrix[i][y_size+1]=-1

        for j in range( y_size+2):
            self.matrix[0][j]=-1
            self.matrix[x_size+1][j]=-1


    def check_side( self ):

        if self.matrix[self.x][self.y+1] == 0 :
            return "UP"
        if self.matrix[self.x+1][self.y] == 0 :
            return "RIGHT"
        if self.matrix[self.x][self.y-1] == 0 :
            return "DOWN"
        if self.matrix[self.x-1][self.y] == 0 :
            return "LEFT"
        else :
            return "STOP"

    def check_dir( self ):

        if self.direction == "UP" and self.matrix[self.x][self.y+1]==0 :
            return "UP"
        elif self.direction == "RIGHT" and self.matrix[self.x+1][self.y]==0:
            return "RIGHT"
        elif self.direction == "DOWN" and self.matrix[self.x][self.y-1]==0:
            return "DOWN"
        elif self.direction == "LEFT" and self.matrix[self.x-1][self.y]==0:
            return "LEFT"
        else:
            return ""

    def start( self, x,y ):

        self.x=1
        self.y=1
        self.cell_count=1
        while ( self.direction != "STOP"):

            print("x,y,dir=[%d,%d,%s]" %(self.x,self.y,self.direction))
            self.update_cell()
            direction = self.check_dir()
            if direction == "":
                self.direction = self.check_side()
            else:
                self.direction = direction

            self.print_matrix()
            print("x,y,dir=[%d,%d,%s]" %(self.x,self.y,self.direction))
            print()
            input("Press Enter Key ...5")

    def update_cell(self):
        if self.direction == "UP" :
            self.y=self.y+1
        elif self.direction == "RIGHT" :
            self.x = self.x+1
        elif self.direction == "DOWN" :
            self.y = self.y-1
        elif self.direction == "LEFT" :
            self.x = self.x-1
        self.matrix[self.x][self.y]=self.cell_count
        self.cell_count+=1

    def print_matrix(self):

        for j in range( len(self.matrix[0])-1,-1,-1 ):
            for i in range(len(self.matrix),):

                print( "%2d" %self.matrix[i][j], end=" ")
            print("")


pt = Point( x_size, y_size )
pt.print_matrix()
pt.start(1,1)




