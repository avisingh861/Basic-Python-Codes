#Factorial using iteration

print("Enter number to find factorial")
n = int(input())
#z=1
def factorial(n):
    z=1
    for i in range(1,n+1):
        print("Factorial at step",i,"is ",z)
        z*=i
        print(z)
print("The factorial of",n,"is",factorial(n))
