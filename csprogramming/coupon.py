from unittest import result

from numpy import c_


cnt, c_val = map( int, input().split() )


list_menu=[]
select_menu=[]
for _ in range(cnt):
    list_menu.append(int(input()))

print(cnt, c_val)
print(list_menu)


    
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
    


print( "*"*20)

for i in range(1, cnt+1):
    print( i )
    C(cnt, i)

sel_menu=[]
max_select=0
for i in range(len(result_list)):
    price = sum([list_menu[x-1] for x in result_list[i] ]) 
    if price <= 5000 :
        max_select=max(max_select, len(result_list[i]))
        sel_menu.append( [result_list[i], price])

print( sel_menu )
print( "max_select::",max_select )

for v in sel_menu:
    if len(v[0]) == max_select:
        print( v[0])



#all2( list_menu )
#print( "*"*20)
#print( select_menu )
        


