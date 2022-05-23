result_list=[]
def C(cnt, n , lt=[]):
    global result_list
    if n == 0:
        result_list.append(sorted(lt))
        return
    elif cnt == 0:
        return
    else:
        lt2=lt.copy()
        C(cnt-1, n,lt)
        lt2.append(cnt) 
        C(cnt-1, n-1,lt2)
    

C(10,2 )
print( len(result_list), result_list )

