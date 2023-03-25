def is_armstrong(n):

digits = str(n)
6 PP/SEM II/2021-22

K. J. Somaiya College of Engineering, Mumbai-77
(A Constituent College of Somaiya Vidyavihar University)
Department of Science and Humanities

total = sum(int(digit)**3 for digit in digits)
return total == n

n = int(input("Enter a number: "))
if is_armstrong(n):
print(n, "is an Armstrong number")
else:
print(n, "is not an Armstrong number")
