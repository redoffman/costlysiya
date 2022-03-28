
in_str=input()
fix_cost, p_cost, price = map(int,in_str.split())


if p_cost >= price:
    print(-1)
else:
    print(fix_cost // ( price - p_cost) +1) 
    
    
