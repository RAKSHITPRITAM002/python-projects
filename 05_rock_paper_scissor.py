import random
while True:
    choice = input('Rock, Paper or Scissors (r/p/s) (q to quit): ').lower()
    if choice == 'q':
        print("Goodbye!")
        break
    if choice not in ('r', 'p', 's'):
        print("Invalid Choice!")
        continue

    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose: {computer}')

    if choice == computer:
        print("It's a tie!")
    elif (choice == 'r' and computer == 's') or (choice == 's' and computer == 'p') or (choice == 'p' and computer == 'r'):
        print("YOU WIN! HOORAY")
    else:
        print("YOU LOSE :(")
    
