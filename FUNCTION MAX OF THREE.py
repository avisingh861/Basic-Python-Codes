def max_three(x,y,z):
  if(x>y and x>z):
    print("The largest number is x and its value is",x)
  elif(y>x and y>z):
    print("the largest number is y and its value is",y)
  else:
      print("the largest number is z and its value is",z)
x= int(input("Enter first Number"))
y= int(input("Enter second Number"))
z= int(input("enter third Number"))
max_three(x,y,z)
