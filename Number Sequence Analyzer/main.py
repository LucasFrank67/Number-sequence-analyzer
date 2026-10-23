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


def prime_checker():
    print("What number do you want to check?")
    result = int(input())
    if result > 1:
        for i in range(result):
            if result % (i + 1) != 0:
                print("The number is prime!")
            else:
                print("The number isn't prime, loser!")
    else:
        print("The number must be greater than 1, loser!")

def main():
    clear_console()
    while True:
        print("NUMBER SEQUENCE ANALYZER!")
        print("1. Fibonacci Sequence\n")
        print("2. Prime Number Checker\n")
        print("3. Multiplication Table\n")
        print("4. Factorial Calculator\n")
        print("5. Collatz Sequence\n")
        print("6. Exit\n")
        try:
            result = int(input())
        except ValueError: 
            print("You must enter a number from 1 to 6. Please try again.\n")
            continue
        match result:
            case 1: 
                fibonacci()
            case 2:
                prime_checker()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass

main()