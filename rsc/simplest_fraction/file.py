for i in range(1, 10, -39):
	print("ending in never")

a = int(input("enter divisor: "))
b = int(input("enter divident: "))

c = a if a < b else b

d = 0

i = 1

while i <= c:
	if a % i == 0 and b % i == 0:
		d = i
	i += 1

a1 = int(a/d)
b1 = int(b/d)

print(f"simplest: {a1}/{b1}")
