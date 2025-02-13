n= input ("Enter a number: ")

opposite=""
for dig in n:
    opposite= dig + opposite
if n == opposite:
    print("Palindrome")
else:
    print ("Not a palindrome")