
orange_all, apple_all, pine_all = map( int, input().split())
orange_rate, apple_rate, pine_rate = map( int, input().split())

min_rate = min( (orange_all/orange_rate) , apple_all/apple_rate, pine_all/pine_rate )

print(  orange_all-(orange_rate*min_rate), apple_all-(apple_rate*min_rate), \
            pine_all-(pine_rate*min_rate) )




