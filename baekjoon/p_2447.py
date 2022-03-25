def pattern( row, column, N):
    
    if((row / N) % 3 == 1 and (column / N) % 3 == 1):
        print(" ",end="") 
    else :
        if( N/3 == 0) :
            print("*",end="")
        else :
            pattern(row, column, N/3)


VAL=9

for i in range(VAL) :
    for j in range(VAL):
        pattern(i, j, VAL)
    print("A")

    
