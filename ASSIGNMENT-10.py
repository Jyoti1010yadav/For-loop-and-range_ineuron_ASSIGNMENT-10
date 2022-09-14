# 1. Write a python script to print MySirG N times on the screen
n=int(input("Enter number of times u want to print"))
for i in range(1,n+1):
    print("MySirG")
print()    

# 2. Write a python script to print first N natural numbers
n=int(input("Enter first N natural numbers you want to print"))
for i in range(1,n+1):
    print(i)
print()    

# 3. Write a python script to print first N natural numbers in reverse order
num=int(input("Enter first N natural numbers in reverse order you want to print"))
for i in range(num,0,-1):
    print(i)
print()    

# 4. Write a python script to print first N odd natural numbers
num=int(input("Enter first N odd natural numbers you want to print"))
for i in range(1,2*num,2):
    print(i)
print()    

# 5. Write a python script to print first N odd natural numbers in reverse order
num=int(input("Enter first N odd natural numbers you want to print in reverse order"))
for i in range(2*num-1,0,-2):
    print(i)
print()    
# 6. Write a python script to print first N even natural numbers
num=int(input("Enter first N even natural numbers you want to print"))
for i in range(2,2*num+2,2):
    print(i)
print()    

# 7. Write a python script to print first N even natural numbers in reverse order
num=int(input("Enter first N even natural numbers you want to print in reverse order"))
for i in range(2*num,0,-2):
    print(i)
print()    

# 8. Write a python script to print squares of first N natural numbers
n=int(input("Enter first N natural numbers squares you want to print"))
for i in range(1,n+1):
    print(i*i)
print()

# 9. Write a python script to print cubes of first N natural numbers
n=int(input("Enter first N natural cubes of numbers you want to print"))
for i in range(1,n+1):
    print(i*i*i)
print()

# 10. Write a python script to print first 10 multiples of N
num=int(input(" Enter num which yu want to print multiplication "))
for i in range(1,num+1):
    print(i*num)
print()    