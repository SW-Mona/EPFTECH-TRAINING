
multi = [0]
num1 = 3
num2 = 5

def multiples(num1,num2):
    total = 0
    for i in range(1000):
        if i%num1 == 0 or i%num2 == 0:
            multi=i
            total = total + i
            print(multi)
    print(total)

multiples(num1,num2)
