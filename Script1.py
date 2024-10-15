import random
import time
from colorama import init, Fore


init(autoreset=True)

def calculations():
    print(Fore.BLUE + "Welcome to the basic aptitude Calculations Test!")
    difficulty = input(Fore.YELLOW + "Choose difficulty level(easy, medium, difficult): ").strip()
    if difficulty == "easy":
        range = (0, 9)
    elif difficulty == "medium":
        range = (0, 20)
    elif difficulty == "difficult":
        range = (0, 99)
    else:
        print("Invalid difficulty(by default:Easy)")
        range = (0, 9)

    while True:
        try:
            time_limit = int(input(Fore.YELLOW + "Enter time limit in seconds (max 120 seconds): "))
            if 1 <= time_limit <= 120:
                break
        except ValueError:
            print(Fore.RED + "Enter between 1 and 120sec")
    
    start_time = time.time()
   

    print(Fore.GREEN + f"Start solving math problems! Difficulty: {difficulty.capitalize()}, Time Limit: {time_limit} seconds.")
    
    rights = 0
    while True:
        if time.time() - start_time > time_limit:
            print(Fore.YELLOW + f"Time's up! You answered {rights} questions correctly.")
            break
        num1 = random.randint(*range)
        num2 = random.randint(*range)
        op = random.choice(['+', '-', '*', '/'])  
        if op == '+':
            question = f"{num1} + {num2}"
            right = num1 + num2
        elif op == '-':
            question = f"{num1} - {num2}"
            right = num1 - num2     
        elif op == '/':
            question = f"{num1 * num2} / {num1}"
            right = num2
        elif op == '+':
            question = f"{num1} + {num2}"
            right = num1 + num2
        elif op == '-':
            question = f"{num1} - {num2}"
            right = num1 - num2
        elif op == '*':
            question = f"{num1} * {num2}"
            right = num1 * num2

        ans = input(Fore.MAGENTA + f"{question} = ")
        
        try:
            if int(ans) == right:
                print(Fore.GREEN + "Correct!")
                rights += 1
            else:
                print(Fore.RED + "Wrong!")
        except ValueError:
            print(Fore.RED + "Invalid input!")
        



calculations()
