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

matrix= [[0 for col in range(y_size)] for row in range(x_size)]

#for x in range(x_size):
#    for y in range( y_size):
#       print( x, y, matrix[x][y])


idx_x=0
idx_y=-1
idx_total=0



def set_metrix( x, y, val, flag=1):

    global idx_x
    global idx_y
    global idx_total
    global matrix

    if x == 0 or y == 0:
        return

    for j in range(y):


        #print("matrix[%d][%d]=%d in set" %(idx_x, idx_y, val))
        matrix[idx_x][idx_y+j*flag]=val
        val=val+1

    idx_y=idx_y+flag*(y-1)

    for i in range(x):

        #print("matrix[%d][%d]=%d in set" %(idx_x, idx_y, val))
        matrix[idx_x+i*flag][idx_y]=val
        val=val+1
    idx_x=idx_x+flag*(x-1)


    if flag == 1 :
        set_metrix( x-1,y-1 , val, -1)
    else:
        set_metrix( x-1, y-1, val, 1 )

    return

#set_metrix( x_size, y_size, 0 )




for n in range(0, min(x_size,y_size)):

    print("N value:",n)
    if  n%2 == 0 :
        flag = 1
    else:
        flag = -1

    for j in range(y_size-n):
        idx_total=idx_total+1
        idx_y = idx_y + flag
        print("matrix[%d][%d]=%d in set" %(idx_x, idx_y, idx_total))
        matrix[idx_x][idx_y]=idx_total




    for i in range(x_size-n-1):
        idx_total=idx_total+1
        idx_x = idx_x + flag
        print("matrix[%d][%d]=%d in set" %(idx_x, idx_y, idx_total))
        matrix[idx_x][idx_y]=idx_total




for x in range(x_size):
    for y in range( y_size):
        print(  x, y, matrix[x][y])


exit
in1=[ int(n) for n in input().split()]

if  len(in1)  == 2 :
    print("result2 value :", matrix[in1[0], in1[1]])
else:
    for x in range(x_size):
        for y in range( y_size):
            if in1[0] == matrix[x][y]:
                print( "result1 xy :", x, y, matrix[x][y])
                break








