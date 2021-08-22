print("Enter number")
try:
    number = int(input())
except ValueError:
    print("Enter Integer")

def collatz(number):
    while(number !=1):
        if((number) % 2 == 0):
            number = number / 2;
            print (number);
        elif((number) %2 != 0):
            number = ((number * 3) +1);
            print (number);
        else:
            print("idk")
collatz(number)


            

        
