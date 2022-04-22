
def add_func( fx, gx ):
    max_len = max( len(fx), len(gx) )
    rx=[ int(0) for _ in range( max_len )]

    for i in range( max_len ):
        if( i < len(fx)) :
            fx_val =  fx[i]
        else:
            fx_val = 0
        if( i < len(gx)) :
            gx_val =  gx[i]
        else:
            gx_val = 0

        rx[i] = fx_val + gx_val

    return rx.copy()

def sub_func( fx, gx ):
    max_len = max( len(fx), len(gx) )
    rx=[ int(0) for _ in range( max_len )]

    for i in range(max_len):
        if( i < len(fx)) :
            fx_val =  fx[i]
        else:
            fx_val = 0
        if( i < len(gx)) :
            gx_val =  gx[i]
        else:
            gx_val = 0
        rx[i] = fx_val -  gx_val

    return rx.copy()



def multi_func( fx, gx ):
  rx=[ int(0) for _ in range(len(fx)+len(gx)-1) ]

  for i in range(len(fx)):
    for j in range(len(gx)):
      rx[i+j]=rx[i+j]+fx[i]*gx[j]

  return rx.copy()

def div_func( fx, gx ):

    result=[]

    rx=[ int(0) for _ in range(len(fx)) ]
    
    for i in range( len(fx)-len(gx)+1 ) :
        print("fx", fx )
        print("gx", gx )

        div_val = fx[len(fx)-1-i] / gx[len(gx)-1] 
        result.insert(0,div_val)
        print("div_val", i, div_val, len(fx)-1-i, len(gx)-1) 
        dx = multi_func([div_val],gx) 
        dx = shift_func( dx, len(fx)-len(gx)-i )
        print( "dx=", dx )
        sub_x = sub_func( fx, dx )

        print( "sub_x=", sub_x )
        
        fx = sub_x 

    return result , fx  

def shift_func( fx, n ):
    rx = fx
    for _ in range(n):
        rx.insert(0,0) 
    return rx







#cnt=int(input())

#for _ in range( cnt ):
#  in_func=[ int(n) for n in input().split()][::-1]
#  result_func =  multi_func( in_func, result_func )
#  #print( result_func)





import sys

result_func=[ 1, 1   ]
for s in sys.stdin:
  s=s.strip("\n")
  print(f"s=[{s}]")
  in_func=[ int(n) for n in s.split( )][::-1]
  #result_func =  multi_func( in_func, result_func )
  #result_func =  add_func( in_func, result_func )
  result_func, result2_func  =  div_func( in_func, result_func ) 
  print( result_func)
  print( result2_func)

#for n in result_func[::-1]:
  #print(n, end=" ")
