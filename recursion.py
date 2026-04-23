# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
	        
# print(factorial(5))

#1. Sum of first n numbers using recursion

def sumof_n(n):
    if n == 1:
        return 1
    else:
        return n + sumof_n(n-1)
print(sumof_n(5))

#2. Print Numbers (Forward) Eg: 1 2 3 4 5

def print_numbers_forward(n):
    if n == 0:  
        return
    print_numbers_forward(n - 1)
    print(n)

print_numbers_forward(5)

#3. Fibonnaci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
terms = 10

for i in range(terms):
    print(fibonacci(i), end=" ")

#4. Power of a Number eg: 2^5

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
    
print(power(2,3))

#5. Reverse a String eg: hello -> olleh

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + s[:-1]
    
print(reverse("HELLO"))

