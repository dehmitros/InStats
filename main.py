import os

# Define color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ORANGE = '\033[33m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Define options menu
options = {
    '1': 'Scripts/TotalMessagesCounter.py',
    '2': 'Scripts/TotalSentMessagesCounter.py',
    '3': 'Scripts/TotalReceivedMessagesCounter.py',
    '4': 'Scripts/graph.py',
    '5': 'Scripts/change_path.py'
}

# Check if path.txt exists, if not prompt user to enter a path
if not os.path.exists('path.txt'):
    while True:
        path = input('Enter the path to your inbox folder: ')
        if os.path.exists(path):
            with open('path.txt', 'w') as f:
                f.write(path)
            break
        else:
            print(Colors.FAIL + 'Invalid path. Please try again.' + Colors.ENDC)
else:
    with open('path.txt', 'r') as f:
        path = f.read()

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome message
print(Colors.HEADER + 'Welcome to InStats!' + Colors.ENDC)
print()

# Loop until the user chooses to exit
while True:
    # Print the options menu
    print(Colors.OKBLUE + 'Please select an option from the following menu:')
    print(Colors.ORANGE + '1. Total Messages' + Colors.ENDC)
    print(Colors.YELLOW + '2. Total Messages sent' + Colors.ENDC)
    print(Colors.ORANGE + '3. Total Messages received' + Colors.ENDC)
    print(Colors.YELLOW + '4. Graph the results' + Colors.ENDC)
    print(Colors.ORANGE + '5. Change the path to the Inbox folder' + Colors.ENDC)
    print(Colors.FAIL + '0. Exit')
    print()

    # Get user input
    choice = input(Colors.OKBLUE + 'Enter choice: ')

    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Process user input
    if choice == '0':
        print(Colors.OKGREEN + 'Thank you for using InStats!' + Colors.ENDC)
        print(Colors.OKBLUE + 'Check it out on GitHub! ' + Colors.ENDC)
        print(Colors.OKGREEN + 'https://github.com/dehmitros/InStats' + Colors.ENDC)
        break
    elif choice == '5':
        while True:
            new_path = input('Enter the new path to your inbox folder: ')
            if os.path.exists(new_path):
                with open('path.txt', 'w') as f:
                    f.write(new_path)
                path = new_path
                break
            else:
                print(Colors.FAIL + 'Invalid path. Please try again.' + Colors.ENDC)
    elif choice in options:
        script_path = options[choice]
        if choice == '1' or choice == '3':
            color = Colors.ORANGE
        else:
            color = Colors.YELLOW
        print(color + f'Running {script_path}...' + Colors.ENDC)
        os.system(f'python {script_path} {path}')
        print()
    else:
        print(Colors.FAIL + 'Invalid choice. Please try again.' + Colors.ENDC)
        print()
