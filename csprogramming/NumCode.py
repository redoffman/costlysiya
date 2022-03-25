#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      redof
#
# Created:     20-03-2022
# Copyright:   (c) redof 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import sys


#line=input()
line=sys.stdin.readline().strip()



print("line len:%d" %(len(line)))

def invalidate( str ):

    return str.isdigit()

def mk_code( str ):

    rt_code=""
    if len(str) <= 1 :
        return rt_code

    for i in ( range(len(str)-1) ):

        sub_value =  int(str[i] ) - int(str[i+1])

        if sub_value == 0 :
            ret_code += "e"
        if sub_value == -1 :
            rt_code += "u"
        elif sub_value == 1 :
            rt_code += "d"
        else :
            rt_code += "n"

    return rt_code

def code_to_score ( str ):

    sum_point = 0 ;
    add_point = 0 ;
    pre_ch =""

    for ch in str :
        if ch == "n":
            add_point = 0
        elif pre_ch == ch :
            add_point = add_point +1
            sum_point = sum_point + add_point
        else:
            add_point = 1
            sum_point = sum_point + add_point

        pre_ch = ch

    return sum_point



if( invalidate(line) == False ):
    print("_ERROR_NOT_DIGIT")
else:
    code=mk_code(line)
    print("code:[%s]" %code)
    print(code_to_score(code))





