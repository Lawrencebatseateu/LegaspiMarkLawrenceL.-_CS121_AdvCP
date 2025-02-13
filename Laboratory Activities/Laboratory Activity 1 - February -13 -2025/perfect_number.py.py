num=int(input("Enter a number: "))
sum_div = 0

for i in range (1, num):
    if num % i==0:
        sum_div += i
if num==sum_div:
    print (num,"is a perfect number")
else:
    print (num,"is not a perfect number")