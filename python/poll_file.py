while True:
    reason = input("Why you like programming? (q to quit): ")
    if reason == "q": break
    with open('polls.txt', 'a') as f:
        f.write(f'{reason}\n')

