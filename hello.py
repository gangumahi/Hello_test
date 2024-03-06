import sys
print("Welcome to my first git python script")
print("Factorial of a number")
def fact(n):
    if n == 1:
         return 1
    else:
         return n*fact(n-1)

n_fact = fact(int(sys.argv[1]))
print("Factorial = ", n_fact)

