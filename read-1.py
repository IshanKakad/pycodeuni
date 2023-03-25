def is_prime(n):

if n < 2:
return False
for i in range(2, int(n**0.5) + 1):
if n % i == 0:
return False
return True

prime_number = 0
composite_number = 0
n = int(input("Enter a number (-1 to stop): "))
while n != -1:
if is_prime(n):
prime_number += 1
else:
composite_number += 1
n = int(input("Enter a number (-1 to stop): "))
print("Number of prime numbers entered:", prime_number)
print("Number of composite numbers entered:", composite_number)
