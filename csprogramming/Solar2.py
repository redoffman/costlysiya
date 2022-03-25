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

matrix= [[0 for col in range(y_size+1)] for row in range(x_size+1)]

#for x in range(x_size):
#    for y in range( y_size):
#       print( x, y, matrix[x][y])


idx_x=0
idx_y=0
idx_total=0



for n in range( 1, min(x_size,y_size) ):

    min_idx_x=n
    min_idx_y=n
    max_idx_x=x_size-n+1
    max_idx_y=y_size-n+1


    if min_idx_x > max_idx_x or min_idx_y > max_idx_y :
        break

    print( "min_idx_x, min_idx_y, n:", min_idx_x, min_idx_y, n)
    print( "max_idx_x, max_idx_y, n:", max_idx_x, max_idx_y, n)

    if( min_idx_x == max_idx_x) and (min_idx_y == max_idx_y):
        idx_total=idx_total+1
        matrix[min_idx_x][min_idx_y]=idx_total
        break

    for j in range(min_idx_y, max_idx_y):
        idx_total=idx_total+1
        print("matrix[%d][%d]=%d in set1" %(min_idx_x,j, idx_total))
        matrix[min_idx_x][j]=idx_total


    for i in range(min_idx_x, max_idx_x):
        idx_total=idx_total+1
        print("matrix[%d][%d]=%d in set2" %(i, max_idx_y, idx_total))
        matrix[i][max_idx_y]=idx_total


    for j in range(max_idx_y,min_idx_y,-1):
        idx_total=idx_total+1
        print("matrix[%d][%d]=%d in set3" %(max_idx_x, j, idx_total))
        matrix[max_idx_x][j]=idx_total


    for i in range(max_idx_x,min_idx_x,-1):
        idx_total=idx_total+1
        print("matrix[%d][%d]=%d in set4" %(i, min_idx_y, idx_total))
        matrix[i][min_idx_y]=idx_total



for y in range( 1, y_size +1):
    for x in range(1, x_size+1):
        print(  "%2d" %matrix[x][y], end=" ")
    print("")


in1=[int(n) for n in input().split()]

if  len(in1)  == 2 :
    print( in1 )
    print("result2 value :", matrix[in1[0]][in1[1]])
else:
    for x in range(1,x_size+1):
        for y in range( 1,y_size+1):
            if in1[0] == matrix[x][y]:
                print( "result1 xy :", x, y, matrix[x][y])
                break


