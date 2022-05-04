def get_d(n):
    val=n%10
    val+=(n//10)%10
    val+=(n//100)%10
    val+=(n//1000)%10
    val+=(n//10000)%10
    val+=n
    return val
    
list_num=[True]*10100
for i in range(1, 10000+1):
    list_num[get_d(i)]=False
for i in range(1, 10000+1):
    if list_num[i] == True:
        print(i)
    