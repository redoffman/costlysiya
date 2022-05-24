result_list=[]
cupon=10000

def  C_ALL( c_list, lt=[] ):
    
    global result_list, cupon
    ret_val = 0 
    
    if sum( lt ) > cupon :
        return    

    if len(c_list) == 0 : 
        if len(lt) > 0 :
            result_list.append(lt)
        return 

   
    lt_first=lt.copy()
    lt_first.append(c_list[0])
    
    C_ALL( c_list[1:], lt_first )  
    C_ALL( c_list[1:], lt.copy() ) 
   
    return 
    
    

menus= [1000,2000,3000,4000,5000,6000,500,300,200]
C_ALL( menus )

print( result_list)

