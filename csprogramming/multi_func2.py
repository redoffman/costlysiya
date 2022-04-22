

def multi_func( fx, gx ):
  rx=[ int(0) for _ in range(len(fx)+len(gx)-1) ]

  for i in range(len(fx)):
    for j in range(len(gx)):
      rx[i+j]=rx[i+j]+fx[i]*gx[j]

  return rx.copy()

result_func=[1]

#cnt=int(input())

#for _ in range( cnt ):
#  in_func=[ int(n) for n in input().split()][::-1]
#  result_func =  multi_func( in_func, result_func )
#  #print( result_func)





import sys

for s in sys.stdin:
  s=s.strip("\n")
  print(f"s=[{s}]")
  in_func=[ int(n) for n in s.split( )][::-1]
  result_func =  multi_func( in_func, result_func )
  print( result_func)

#for n in result_func[::-1]:
  #print(n, end=" ")
