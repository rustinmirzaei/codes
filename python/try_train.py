
def get_value():
	return int(input("Enter an integer: "))



def exer2():
	try:
		x = get_value()
	except ValueError:
		print("Value Error")
	

def exer1():
    try:
        x = int(input("Enter an integer: "))
        y = int(input("Enter another integer: "))
    except ValueError:
        print("the value cannot parse as an integer.")
    else:
        res = x + y
        print(f"{x} + {y} = {res}")



exer2()
