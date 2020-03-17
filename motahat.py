import os
os.system('clear')


print("\033[1;31m _____       ___  ___       ___  __    __") 
print("\033[1;32m|_   _|     /   |/   |     /   | \ \  / /") 
print("  \033[1;31m| |      / /|   /| |    / /| |  \ \/ / ") 
print("  \033[1;32m| |     / / |__/ | |   / / | |   }  {  ") 
print("  \033[1;31m| |    / /       | |  / /  | |  / /\ \ ") 
print('  \033[1;32m|_|   /_/        |_| /_/   |_| /_/  \_\ ')

A='\033[1;33m'
B="\033[1;31m"
C="\033[1;32m"

print(A)
name=input("Enter Name: ")
print(B)
email=input("Enter Email: ")
number =0
while number<100:
    number=number+1
    print(C)
    print('[✅]',name+str(number)+email)
