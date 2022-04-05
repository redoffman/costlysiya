
import string


def get_value(list, i,j ):

    if i < 0 or i >= len(list) or j < 0 or j >=len(list[i]):
        return 0
    else :
        if list[i][j] == ".":
            return 0
        else : 
            return int(list[i][j])

def get_sum_side( list, i, j):

    sum_val = get_value( list, i-1, j-1) + get_value( list, i, j-1 ) + get_value(list, i+1, j-1)
    sum_val += get_value( list, i-1, j) + get_value(list, i+1, j)
    sum_val += get_value( list, i-1, j+1) + get_value( list, i, j+1 ) + get_value(list, i+1, j+1)

    if sum_val < 10 :
        return "{}".format(sum_val)  
    else :
        return "M"

count=int(input())



list=[]
for i in range( count ):
    list.append( input() )

print( list )

result=[]
for i in range( len(list) ):
    str=""
    for j in range(len(list[i])):
        #print( i,j, list[i][j] )
        str+=get_sum_side( list, i, j)
    result.append( str)

print(result)

for str in result:
    for ch in str :
        print( ch, end="")
    print()

    

         

        

