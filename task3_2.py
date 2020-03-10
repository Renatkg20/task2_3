a = int(input("Enter the temp F "))

def temp(a):
	return ((a - 32) * 5/9)

result = round(temp(a), 2)
print(f"{result} C")