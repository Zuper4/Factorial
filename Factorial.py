print("\nThis is a program that will give you the factorial of the number you will input.")
print("If you don't know what the factorial of a number means well,")
print("The factorial of x is x*x-1*x-2*...*1. So we multiply the number by the number before him again and again until we reach 1.")

number = int(input("\nI will calculate the factorial of :"))

factorial = 1

if number < 0 :
    print("Factorial doesn't exist for negative numbers.")

elif number == 0 :
    print("The factorial of 0 is 1 !")    

else :
    for i in range(1, number + 1):

        factorial = factorial * i
        
    print("The factorial of " +str(number)+ " is " +str(factorial))

