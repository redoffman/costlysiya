
import string

#for w in string.ascii_lowercase : 
#   print( f"w={w}, ord(w)={ord(w)-87}")

#for i in "0123456789":
#   print(f"i={i} value={i}")


def get_val(c):
    if  c.isdigit() :
        return int(c)
    else :
        return  ( ord(c)-87)

in_str="0012340010cz00zzz00"

max_val=0
curr_val=0
for ch in in_str:
    print ( f"{ch}  ->  {get_val(ch)}")
    val = get_val(ch)
    
    if val == 0 :
        max_val=max( max_val, curr_val)
        curr_val=0
        print( f"max_val  in for {max_val}")
        
    else :
        curr_val = curr_val + val 
max_val = max( max_val, curr_val )
print( f"max_value={max_val}")