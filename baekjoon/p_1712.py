import math
in_str=input()
fix_cost, p_cost, price = map(int,in_str.split())

i=0;
check=True

if p_cost >= price:
    print(-1)
else:
    print(math.ceil((fix_cost+1) / ( price - p_cost))) 
    
    
