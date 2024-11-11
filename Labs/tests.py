# TASK 1:
n = int(input("Enter your number here:"))
def calculate_square_and_cube(n):
    x = lambda n: n**2
    y = lambda n: n**3
    return x(n),y(n)
x, y = calculate_square_and_cube(n)
print(x,y)

# TASK 2:
def sum_up_to(n):
    if n==0:
        return 0
    else:
        return n + sum_up_to(n-1)
user = int(input("enter a number to sum:"))
print (sum_up_to(user))



