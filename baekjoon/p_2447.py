def print_star(n):

    if n == 3:
        print("***", end="")
        print("* *", end="")
        print("***", end="")
    else:
        print_star(int(n/3)) 

print_star(int(input()))