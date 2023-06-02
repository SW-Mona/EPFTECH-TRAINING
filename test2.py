
sum = 0

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-2)+fibonacci(x-1)

for i in range(34):  
    if i > 0 and fibonacci(i)<4000000:
        if fibonacci(i) % 2 == 0:
            sum = sum + fibonacci(i)
            print(fibonacci(i))
print("SUM = ",sum)