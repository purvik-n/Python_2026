import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',';',':',"'",'"',',','.','<','>','/','?','\\','|','`','~']

print("Welcome to the Password Generator!")

n_letters = int(input("How many letters would you like in your password?"))
n_numbers = int(input("How many numbers would you like in your password?"))
n_symbols = int(input("How many symbols would you like in your password?"))

password = []

for _ in range(n_letters):
    password.append(random.choice(letters))

for _ in range(n_numbers):
    password.append(random.choice(numbers))

for _ in range(n_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

password = "".join(password)

print("Your password is:", password)
