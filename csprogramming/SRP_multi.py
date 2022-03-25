#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      redof
#
# Created:     19-03-2022
# Copyright:   (c) redof 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys



#List=[ "R", "R", "S", "S", "S"]
line=sys.stdin.readline()
List=line.split()


def SRP_Game ( s, r , p ):

    if ( s and r and p ):
        return "SRP_ALL"
    elif ( r and s  ):
        return "R_WIN"
    elif ( s and p  ):
        return "S_WIN"
    elif ( p and r ):
        return "P_WIN"
    elif ( s  ):
        return "S_ALL"
    elif ( r  ):
        return "R_ALL"
    elif ( p  ):
        return "P_ALL"
    else :
        return "_ERR"


s=False
r=False
p=False


for val in List:
    if val == "S":
        s=True
    elif val == "R":
        r=True
    elif  val == "P":
        p = True


print( "Result2: ", SRP_Game( s, r, p ))