def read_numbers():
  num1=int(input( print("enter the number 1")))
  num2=int(input( print("enter the number 2")))
  return num1,num2
def sum_of_numbers():   
    sum = num1+num2 
    return sum
    

def sub_of_numbers():  
  sub = num1-num2
  return sub


num1,num2 = read_numbers()
sum = sum_of_numbers()
sub = sub_of_numbers()
print("sum of numbers is",sum)
print("sub of numbers is",sub)
print(sum)
