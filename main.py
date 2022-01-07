# Write a Python Function to generate all the factors of a number
def print_factors(x):

   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

n=int(input())

print_factors(n)