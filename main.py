import os
import subprocess
import platform
from termcolor import colored  # Import termcolor here

try:
    from termcolor import colored
except ImportError:
    subprocess.run(['pip', 'install', 'termcolor'])
    from termcolor import colored

def print_banner():
    print()
    print()
    print()
    print(colored(r""" $$$$$$\                          $$\                     
$$ ___$$\                         \__|                    
\_/   $$ |$$$$$$\$$$$\   $$$$$$\  $$\  $$$$$$\   $$$$$$\  
  $$$$$ / $$  _$$  _$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ 
  \___$$\ $$ / $$ / $$ |$$ /  $$ |$$ |$$ |  \__|$$$$$$$$ |
$$\   $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ |      $$   ____|
\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |$$ |$$ |      \$$$$$$$\ 
 \______/ \__| \__| \__|$$  ____/ \__|\__|       \_______|
                        $$ |                              
                        $$ |                              
                        \__|                              """, 'red'))
    print()
    print()
    print()

def clear_console():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_console()

def process_line(line):
    email, password, token = line.strip().split(':')
    return email, password, token

def print_and_save(data, filename, message, delay=0.05):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + '\n')
            print(colored(f"{message} writing to '{filename}': {item}", 'green'), end='', flush=True)
            print()
        print()

def main():
    print_banner()
    use_tokens_file = input(colored("Do you want to use 'tokens.txt'? (y/n): ", 'green')).lower()

    if use_tokens_file == 'y':
        input_file = 'tokens.txt'
    else:
        input_file = input(colored("Enter the path to the input file: ", 'green'))

    clear_console()

    try:
        with open(input_file, 'r') as file:
            data = [line.strip() for line in file]

        emails = []
        passwords = []
        tokens = []

        for line in data:
            email, password, token = process_line(line)
            emails.append(email)
            passwords.append(password)
            tokens.append(token)
        if not os.path.exists('data'):
            os.makedirs('data')
        print_and_save(emails, 'data/emails.txt', 'Emails')
        print_and_save(passwords, 'data/passwords.txt', 'Passwords')
        print_and_save(tokens, 'data/tokens.txt', 'Tokens')

    except FileNotFoundError:
        print(colored(f"Error: File '{input_file}' not found.", 'red'))
    except Exception as e:
        print(colored(f"Error: {e}", 'red'))

    print_banner()

if __name__ == "__main__":
    main()
