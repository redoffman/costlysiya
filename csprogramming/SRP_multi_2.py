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


#----------------------------------------------------------------------
# S , R , P


SRP={"S" : 0x01, "R": 0x02 , "P": 0x4 }
SRP_Resutl=["_ERR","S_ALL","R_ALL","R_WIN","P_ALL","S_WIN","P_WIN","SRP_ALL" ]


result=0x00
for  val in List:

    # bit  operation
    result = result | SRP[val]
    #print ( "%x %x" %( result, SRP[val]))


print( "Result [%x] , [%s]" %(result, SRP_Resutl[result]))



