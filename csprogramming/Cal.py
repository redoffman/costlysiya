#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      redof
#
# Created:     21-03-2022
# Copyright:   (c) redof 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#input_month_count=input()
input_month_count=4
#input_month_day=input()
input_month_day="31 28 31 30"
#input_first_week=input()
input_first_week="Sat"


month_count = int(input_month_count)

list_month_day = [0] + [int(d) for d in input_month_day.split()]
first_week=input_first_week



def get_week_day( month, day):

    global month_count
    global list_month_day
    week_dic = { "Sun":0, "Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6 }
    week_list = [ "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    sum_days=0

    if( month < 0 or  month_count < month ):
        return "None_Month"
    if( day < 0 or list_month_day[month] < day ) :
        return "None_Day"

    for i in range(1, month):
        sum_days += list_month_day[i]

    sum_days = sum_days + day

    week_result = week_list[(sum_days+week_dic[input_first_week]-1)%7]
    print( "sum_day :: %d" %sum_days)

    return week_result


print( "month_count", month_count )
print( "list_month_day ::", list_month_day  )
print( "First Week :: "+input_first_week )


input_test1="5 15"
test_month, test_day = map( int, input_test1.split())
print( "test1:[%d.%d][%s]" %(test_month,test_day, get_week_day(test_month, test_day)))


input_test1="1 2"
test_month, test_day = map( int, input_test1.split())
print( "test2:[%d.%d][%s]" %(test_month,test_day, get_week_day(test_month, test_day)))


input_test1="3 22"
test_month, test_day = map( int, input_test1.split())
print( "test2:[%d.%d][%s]" %(test_month,test_day, get_week_day(test_month, test_day)))


