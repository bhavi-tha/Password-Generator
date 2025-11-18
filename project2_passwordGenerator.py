import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
print("welcome to the password generator!")
n_letters=int(input("how many letters do you want?"))
n_symbols=int(input("how many symbols do you want?"))
n_numbers=int(input("how many numbers do you want?"))
password = ""#simple way
password_list=[]#password is going to be print in a list
for i in range(1,n_letters+1):
    char= random.choice(letters)
    password_list += char
for i in range(1,n_symbols+1):
    char= random.choice(symbols)
    password_list += char
for i in range(1,n_numbers+1):
    char= random.choice(numbers)
    password_list+= char
print(password_list)
random.shuffle(password_list)#password is going to be print in twice as list by shuffling
print(password_list)#again print the shuffled password_list in a simple way
password=""
for char in password_list:
    password += char
print(password)

