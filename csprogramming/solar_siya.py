val=1
def draw_edge(xstart,ystart,xend,yend):
    global val,list

    print( xstart, ystart, xend, yend)

    for j in range(ystart,yend+1):
        if list[xstart][j]==0:
            list[xstart][j]=val
            val=val+1
        else:
            continue

    for i in range(xstart+1,xend+1):
        if list[i][yend]==0:
            list[i][yend]=val
            val=val+1
        else:
            continue

    for j in range(yend-1,ystart-1,-1):
        if list[xend][j]==0:
            list[xend][j]=val
            val=val+1
        else:
            continue
    for i in range(xend-1,xstart,-1):
        if list[i][ystart]==0:
            list[i][ystart]=val
            val=val+1
        else:
            continue

def draw_edge2(xstart,ystart,xend,yend):
    global val,list

    if ( xstart > xend ) or ( ystart > yend ):
        return 

    for j in range(ystart,yend+1):
            list[xstart][j]=val
            val=val+1
        
    for i in range(xstart+1,xend+1):
            list[i][yend]=val
            val=val+1
        
    for j in range(yend-1,ystart-1,-1):
            list[xend][j]=val
            val=val+1
    
    for i in range(xend-1,xstart,-1):
            list[i][ystart]=val
            val=val+1
        

def find(stdin):
    global list,N,M
    if len(stdin) == 2:
        coordinate = [int(n) for n in stdin]

        if coordinate[0] > N or coordinate[1] > M or coordinate[0] <= 0 or coordinate[1] <= 0:
            print("0 0")
        else:
            print("%d" %(list[coordinate[0]][coordinate[1]]))

    elif len(stdin) == 1:
        num = int(stdin[0])
        for i in range(1, N+1):
            for j in range(1, M+1):
                if list[i][j] == num:
                    print(i,j)
                    return
        print("0 0")
    else:
        print("0 0")


def find2(data):
    global list,N,M
    
    if len(data) == 1:
        num = int(data[0])
        for i in range(1, N+1):
            for j in range(1, M+1):
                if list[i][j] == num:
                    print(i,j)
                    return
        print("0 0")
    else :
        x, y  = map( int, data)

        if (  x <= 0 or  N < x ) or ( y <= 0 or  M < y  ):
            print("0 0")
        else:
            print( "%d" %list[x][y] )



N,M = map(int,input().split())
list=[ [0 for i in range(M+1)] for j in range(N+1)]

for i in range(1, min(N,M)+1 ):
    if i==1:
        draw_edge(i,i,N,M)
    else:
        draw_edge(i,i,N-(i-1),M-(i-1))
###################################################
for j in range(1,M+1):
    for i in range(1,N+1):
        print("%3d" %list[i][j], end=" " )
    print()

def debug():
    global list, N, M
    print( "start.. debug1()")
    for n in range(0, N*M+2):
        check = False
        for i in range( 1, N+1):
            for j in range( 1, M+1):
                if list[i][j] == n :
                    check = True
                    break
       
        if check == False :
            print ( f"False Number = {n}")    
            
    print( "start.. debug2()")
    for i in range( 1, N+1):
        for j in range( 1, M+1):
            if list[i][j] < 1 :
                print( f"list {i},{j} = {list[i][j]}")
    
    print( " end of debug() ")
#debug()

#print(list)

#for n in range( N*M +10 ):
#   print( f"{n} -> ", end="")
#   find2( f"{n}".split() )
#for i in range( 0 , N+2 ):
#   for j in range( 0, M+2):
#       print ( f"{i}, {j} => ", end="")
#       find2 ( f"{i} {j}".split() )

#####################################################



stdin1=input().split()
stdin2=input().split()
stdin3=input().split()
stdin4=input().split()

find(stdin1)
find(stdin2)
find(stdin3)
find(stdin4)

debug()




