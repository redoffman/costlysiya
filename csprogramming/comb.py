result_list=[]
def C(cnt, n , lt=[]):
    global result_list
    if n == 0:
        result_list.append(lt)
        return
    elif cnt == 0:
        return
    else:
        lt2=lt.copy()
        lt2.append(cnt) 
        C(cnt-1, n-1,lt2)
        C(cnt-1, n,lt)
        

result_list=[]
cupon=500

def  C_ALL( c_list, lt=[] ):
    
    global result_list, cupon
    ret_val = 0 
    
    if sum( lt ) > cupon :
        return 0   

    if len(c_list) == 0 : 
        if len(lt) > 0 :
            result_list.append(lt)
            return 1
        else :
            return 0 

   
    lt_first=lt.copy()
    lt_first.append(c_list[0])
    C_ALL( c_list[1:], lt_first )
    C_ALL( c_list[1:], lt.copy() )
    
    return 0


C_ALL( [1,2,3,4 ] )

print( result_list)


