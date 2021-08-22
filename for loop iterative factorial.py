factorial = 1
print("Enter number to find factorial")
num = int(input())
for i in range(1,num+1):
   factorial = factorial*i
   print("IFactorial at step",i,"is ",factorial)
print("The factorial of",num,"is",factorial)
