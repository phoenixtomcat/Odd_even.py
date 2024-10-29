# prompt the user to enter a number
print("Enter a number:")
number = int(input())

#check if the number is odd or even
modulo_operation = number % 2
if modulo_operation > 0:
  print("This is an odd number.")
else:
  print("This is an even number.")