def sum_rec (num, num1):
    if num == 0:
        print(num1)
        return num1
        
    else:    
        sum_rec(num-1,num1+1)
        

num = int(input('Введите число: '))
num1 = int(input('Введите число: '))

sum_rec(num,num1)


print(num1)
