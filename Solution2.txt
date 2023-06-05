a = 1
sum = 0

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-2)+fibonacci(x-1)  
   
while a < 4000000:
    
        if a > 0 and fibonacci(a)<4000000:
            a = a + 1
            #print(fibonacci(a))
            if fibonacci(a) % 2 == 0:
                sum = sum + fibonacci(a)
                print(fibonacci(a))
        else:
             break
print("SUM = ",sum)
    