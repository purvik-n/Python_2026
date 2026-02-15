def multiplication_table(a,b):
    c = a*b
    return c
    
num=int(input("enter the number"))
for i in range(1,11):
    print(f"{num} x {i} = {multiplication_table(num,i)}")