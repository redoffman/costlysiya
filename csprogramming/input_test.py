
import sys

print( " Press Ctrl+d for exit" );
input_list=[]
for s in sys.stdin:
  s=s.strip("\n")
  print(f"s=[{s}]")
  input_list.append(s)

print(input_list)

