num_list : list = []
user_name : str = input("what your name:")
for x in range(1 , 4):
    num : int = int(input(f"write your {x} favorite number:"))
    num_list.append(num)
print(f"\nHello, {user_name} Let's explore your favorite number:")
for item in num_list:
    if item % 2 == 0:
        print(f"The number {item} is even")
    else:
        print(f"The number {item} is odd")

for item in num_list:
    print(f"The number {item} and its square: ({item}, {item ** 2})")
    sum_of_num: int = sum(num_list)
print(f"Amazing! The sum of your favorite number is: {sum_of_num}")

is_prime = True
if sum_of_num <= 1:
    is_prime = False
for x in range (2, sum_of_num):
    if sum_of_num % x == 0:
        is_prime = False
if is_prime == False:
    print(f"great job! The number {sum_of_num} is not a prime number.")
else:
    print(f"wow! the number {sum_of_num} is a prime number.")   
