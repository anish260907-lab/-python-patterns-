# Right angle triangle pattern
import math


for i in range(1,6):
    print("*" * i)

# Inverted right angle triangle pattern
for i in range(5,0,-1):
    print("*" * i)

# Pyramid pattern
for i in range(1,6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# inverted pyramid pattern
for i in range(5,0,-1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# Diamond pattern
for i in range(1,6):
    print(" " * (5 - i) + "*" * (2 * i - 1))    
for i in range(4,0,-1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# Hollow square pattern
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Full square pattern
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# Right angle triangle pattern with numbers
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Inverted right angle triangle pattern with numbers
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Floyd's triangle pattern
num = 1
for i in range(1,6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# Left half pyramid pattern
for i in range(1,6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Hollow pyramid pattern
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Hollow diamond pattern
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(4,0,-1):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# hollow diamond pattern with numbers
num = 1
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(num, end="")
        else:
            print(" ", end="")
    num += 1
    print()
num = 4
for i in range(4,0,-1):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(num, end="")
        else:
            print(" ", end="")
    num -= 1
    print()

# Butterfly pattern
for i in range(1,6):
    print("*" * i + " " * (10 - 2 * i) + "*" * i)
for i in range(4,0,-1):
    print("*" * i + " " * (10 - 2 * i) + "*" * i)

# Hollow number pyramid pattern
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end="")
        else:
            print(" ", end="")
    print()

# Full star pyramid pattern
for i in range(1,6):
    print("* " * i)

# Inverted full star pyramid pattern
for i in range(5,0,-1):
    print("* " * i)

# Left alligned pyramid pattern
for i in range(1,6):
    print("* " * i)

# Right alligned pyramid pattern
for i in range(1,6):
    print(" " * (5 - i) + "* " * i)

# Pascal's triangle pattern
for i in range(5):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

# ZIGZAG pattern
for i in range(1,6):
    for j in range(1, 6):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Hourglass pattern
for i in range(5,0,-1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
for i in range(2,6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# h
# Hollow Diamond pattern with numbers
num = 1
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(num, end="")
        else:
            print(" ", end="")
    num += 1
    print()
num = 4
for i in range(4,0,-1):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(num, end="")
        else:
            print(" ", end="")
    num -= 1
    print()

# Hollow rhombus pattern
for i in range(1,6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Number pyramid pattern
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Reverse number pyramid pattern
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Diamond pattern with numbers
for i in range(1,6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))
for i in range(4,0,-1):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))

# Diamond pattern with stars
for i in range(1,6):
    print(" " * (5 - i) + "* " * i)
for i in range(4,0,-1):
    print(" " * (5 - i) + "* " * i)

# Full pyramid pattern with numbers
for i in range(1,6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))

# Checkerboard pattern
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Hollow circle pattern
import math
for i in range(1,6):
    for j in range(1, 6):
        if math.dist((i, j), (3, 3)) < 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Triangle pattern with numbers
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Rhombus pattern with numbers
for i in range(1,6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))
for i in range(4,0,-1):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))    

# decreasing number pattern
for i in range(5,0,-1):
    print(" ".join(str(x) for x in range(1, i + 1)))

# Hollow inverted pyramid pattern
for i in range(5,0,-1):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or j == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Cross pattern
for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Number inverted pyramid pattern
for i in range(5,0,-1):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))

# Right angle triangle pattern with stars
for i in range(1,6):
    print(" "*(5 - i) + "* " * i)

# Left angle triangle pattern with stars
for i in range(1,6):
    print("* " * i)

# Hollow triangle pattern with stars
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Upside down triangle pattern with stars
for i in range(5,0,-1):
    print(" "*(5 - i) + "* " * i)

# Parallelogram pattern with stars
for i in range(5):
    print(" " * (5 - i) + "* " * 5)

# Inverted parallelogram pattern with stars
for i in range(5):
    print(" " * i + "* " * 5)

# Reverse hollow diamond pattern
for i in range(5,0,-1):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))
for i in range(2,6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))    

# Inverted hollow pyramid pattern with stars
for i in range(5,0,-1): 
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Full hollow diamond pattern
for i in range(1,6):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(4,0,-1):
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Rectangle of numbers
for i in range(1,6):
    for j in range(1, 6):
        print(j, end="")
    print()

# Reverse star pattern
for i in range(5,0,-1):
    print("* " * i)

# Pyramid of numbers 
for i in range(1,6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))