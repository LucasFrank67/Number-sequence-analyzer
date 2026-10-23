import math;
import os;

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def fibonacci():
    clear_console()
    print("Enter how long you want the Fibonacci Sequence?")
    result = int(input())
    a,b = 0,1
    c = None
    print(a)
    print(b)
    for _ in range(result - 2):
        c = a + b
        a = b
        b = c
        print(c)



def prime_checker(result):
    if result < 2:
        return False
    for i in range(2, int(result**0.5) + 1):
        if result % i == 0:
            return False
    return True
    
def prime():
    print("What number do you want to check?")
    result = int(input())
    is_prime = prime_checker(result)
    if is_prime == True:
        print("This is a prime number!")
    elif is_prime == False:
        print("This is NOT a prime number!")



def prime_range():
    print("Starting number: ")
    result1 = int(input())
    print("Ending number: ")
    result2 = int(input())

    numbers = []

    for num in range(result1, result2 + 1):
        is_prime = prime_checker(num)
        if is_prime:
            numbers.append(num)
    for i in numbers:
        print(i, end=", ")

def multiply():
    print("Number: ")
    result1 = int(input())
    print("Length: ")
    result2 = int(input())

    for i in range(1, result2 + 1):
        print(f"{result1} x {i} = {result1 * i}")


def factorial():
    print("What number do you want the factorial of?")
    result = int(input())

    for i in range(1, result):
        result *= i
    print(result)

def collatz():
    print("Give a positive integer.")
    result = int(input())

    yes = []

    while result != 1:
        if result % 2 == 0:
            result = result / 2
        else:
            result = (result * 3) + 1
        yes.append(result)
    print(f"{len(yes)} steps were needed.")

def main():
    clear_console()
    while True:
        print("NUMBER SEQUENCE ANALYZER!")
        print("1. Fibonacci Sequence\n")
        print("2. Prime Number Checker\n")
        print("3. Prime Number Range\n")
        print("4. Multiplication Table\n")
        print("5. Factorial Calculator\n")
        print("6. Collatz Sequence\n")
        print("7. Exit\n")
        try:
            result = int(input())
        except ValueError: 
            print("You must enter a number from 1 to 6. Please try again.\n")
            continue
        match result:
            case 1: 
                fibonacci()
            case 2:
                prime()
            case 3:
                prime_range()
            case 4:
                multiply()
            case 5:
                factorial()
            case 6:
                collatz()
            case 7:
                pass

main()