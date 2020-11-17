
name = input("Enter your name: ")

with open('guest.txt', 'a') as f:
    f.write(f'{name}\n')
