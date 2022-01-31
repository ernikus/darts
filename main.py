def rand_nums():
    import random

    num = random.randint(-10, 10)
    
    return num
    
def dart_board(x, y, points):

    line = pow(x, 2) + pow(y, 2)

    if line <= 1:
        print("You hit INNER CIRCLE!")
        print("*+10 POINTS*")
        points += 10
    elif line <= pow(5, 2):
        print("You hit MIDDLE CIRCLE!")
        print("*+5 POINTS*")
        points += 5
    elif line <= pow(10, 2):
        print("You hit OUTER CIRCLE!")
        print("*+1 POINTS*")
        points += 1
    else:
        print("You hit the WALL!")
        print("*+0 POINTS*")

    return points

    # inner circle       = 10 points, radius = 1
    # middle circle      = 5 points,  radius = 5
    # outer circle       = 1 point,   radius = 10
    # outside the target = 0 points,  radius = rest

points = 0

for i in range(3):
    x = rand_nums()
    y = rand_nums()
    points = dart_board(x, y, points)

print("Your Points: ", points)

#raise Exception("Meaningful message indicating the source of the error")