
while True:
    name = input("Enter your name (q to quit): ")
    if name == "q": break
    print(f"Hello {name}")
    with open('guest_book.txt', 'a') as f:
        f.write(f'{name} visit the program.\n')
