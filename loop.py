#make a multiplication table for a integer
#for loop
n = int(input("enter the number = "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
#to find wether the given no. is armstrong or not
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return n == armstrong_sum

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#to write a program wether the given no. is prime or not
def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
#a program to fin wether the given no. is palindrome or not
def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)

    # Compare the string with its reverse
    return num_str == num_str[::-1]

user_input = int(input("Enter a number: "))
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
    # harmonic series
def harmonic_series(a, d, n):
    for i in range(n):
        print(1 / (a + i * d))

n = int(input("Enter the number of terms: "))
a = int(input("Enter the starting term: "))
d = 1
harmonic_series(a, d, n)
# write a prgram to generate 5 random integer no. between 1 to 100
import random

#(inclusive)
random_number =random.randint(1, 100)

print(f"Random number between 1 and 100: {random_number}")
#write a program to generate the reverse order of a given  no.

original_list = [1, 2, 3, 4, 5]# mene isme slicing ka use kia hai
reversed_list = original_list[::-1]
print(reversed_list)

# a program to concentrate the string "vijay" and "chouan"
#2 string ko concentrate karke  banaya hai
string1 = "vijay"
string2 = "chouan"
result = string1 + string2
print(result)
# a program to extract last name from "vijay chouan" string
# pure name se last wale naaam ko extract karte hai sring me
full_name = "vijay chouan"
name_parts = full_name.split()
last_name = name_parts[-1]
print(last_name)
# write a program to generate a triangle of numbers
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()
# write a program to find sum of all integer no. greater than 100 and divisible by 7

def age (current_year,birth_year):
   print ("current_year 2024","birth_year 2004",current_year-birth_year)
age(2024,2004)

#write a program to find the sum of all integer no. greater than 100 and divisible by 7
# minimum an maximum values:
min_val = 101  # <100
max_val = 200  # largest no.

total_sum = 0

for num in range(min_val, max_val + 1):
    if num % 7 == 0:
        total_sum += num

# Print the result
print("The sum of all integers greater than 100 and divisible by 7 is: ",total_sum)

# write a method defination to find the simple intrest
def calculate_simple_interest(principal, rate, time):

    interest = principal * rate * time
    return interest

principal_amount = 1000
annual_interest_rate = 0.05  # 5% expressed as 0.05
time_period_years = 3

simple_interest = calculate_simple_interest(principal_amount, annual_interest_rate, time_period_years)
print(f"Simple interest: ${simple_interest:.2f}")

#taking out 5 random integers out of 100
#easier way to find out 5 random integers out of 100
import random

print(random.sample(range(1,100),5))
