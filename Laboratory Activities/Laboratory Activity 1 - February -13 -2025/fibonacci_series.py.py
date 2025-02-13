n=int(input("Enter the number of terms: "))
a, b= 0, 1

if n<=0:
    print ("Enter a Positive Integer")
else:
    print("Fibonacci Series: ",a, end=" ")
    for i in range (n-1):
        print (b, end= " ")
        a,b = b, a + b


