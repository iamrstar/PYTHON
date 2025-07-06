number = 4
factorial = 1

original_number = number  # To keep the original value for display
while number > 0:
    factorial *= number
    number -= 1

print("Factorial of", original_number, "is:", factorial)
