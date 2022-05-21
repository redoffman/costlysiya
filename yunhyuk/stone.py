

def shift_stone( stones):

    first_black=-1
    count=0

    print(stones)

    for i in range(len( stones )):
        if stones[i] == 1 and first_black < 0:
            first_black = i
        elif stones[i] == 0 and first_black >= 0 :
            stones[i]=1
            stones[first_black]=0
            first_black += 1
            count += 1
            print(stones)

    return count

def stone(stones):

    print( "stone1" )
    stones1=stones.copy()
    cnt1 = shift_stone( stones1)
    
    print( "stone2" )
    stones2=stones.copy()
    stones2.reverse()
    cnt2 = shift_stone( stones2)  

    print( "stone3" )
    stones3=stones.copy()
    for i in range(len(stones3)):
        if stones3[i] == 0:
            stones3[i] = 1
        else :
            stones3[i] = 0
    cnt3 = shift_stone( stones3)  

    print( "stone4" )
    stones4=stones.copy()
    for i in range(len(stones4)):
        if stones4[i] == 0:
            stones4[i] = 1
        else :
            stones4[i] = 0
    stones4.reverse()
    cnt4 = shift_stone( stones4)

    return min( cnt1, cnt2, cnt3, cnt4 ) 


in_stones=[0,1,1,0,0,0,1,0,1]
print( "min ::" , stone( in_stones))

