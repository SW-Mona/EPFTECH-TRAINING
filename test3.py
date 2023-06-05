x = 600851475143
y = 2

while x != 1:
    remainder = x%y
    if remainder == 0:
        x = x/y
        print(y)
    else:
        y +=1