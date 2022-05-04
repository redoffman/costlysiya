num=int(input())

def get_num(n):
    cnt=0
    val=2
    for i in range(int((n**0.5)/2),n+1):
        if n <= (i*(i+1))/2:
            val=i+1 
            cnt= n - (i*(i-1))//2 
            break
    if val%2 == 1:
        print( "%d/%d"%(cnt, val-cnt))
    else:
        print( "%d/%d"%( val-cnt, cnt))
 
get_num(num)