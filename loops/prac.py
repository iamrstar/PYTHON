number = 18
is_prime = True

for i in range (2, number):
    if (number%i)==0:
      is_prime = False
      break
if is_prime:
   print(number, 'is is prime a number') 
else:
   print(number, "is not a prime number") 
