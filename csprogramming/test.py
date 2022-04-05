

def func():
    global COL, ROW, good_array
    print("COL::", COL)
    print("ROW::", ROW)
    print("good array::", good_array)



COL=7
ROW=5
good_array = [[0 for i in range(COL)] for j in range(ROW)]

print( "good_array=", good_array)

good_array[2][3]=23
good_array[3][2]=32
print( "good_array=", good_array)

for j in range(COL ):
    for i in range( ROW):
        print("%2d"% good_array[i][j], end=" " )
    print()


func()


