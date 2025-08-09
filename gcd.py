# GCD using decrementing loop

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Ensure positive values
x = abs(x)
y = abs(y)

# Start from the smaller number and go downwards
for i in range(min(x, y), 0, -1):
    if x % i == 0 and y % i == 0:
        print(f"GCD is {i}")
        break
