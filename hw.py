def multiply_one(a, b):
    return a * b

def multiply_n(a, b):
    result = 0

    for i in range(b):
        result = result + a

    return result


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Using 1 iteration:", multiply_one(num1, num2))
print("Using N iterations:", multiply_n(num1, num2))