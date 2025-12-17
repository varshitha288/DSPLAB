import datetime

now = datetime.datetime.now()
print("Current date and time:", now)


#2
first = input("Enter first name: ")
last = input("Enter last name: ")

print(last, first)'''

#3
n = int(input("Enter a number: "))

result = n + int(str(n)*2) + int(str(n)*3)
print("Result:", result)

'''#4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print(3 * (a + b + c))
else:
    print(a + b + c)

#5
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x + y) ** 2
print("Result (x+y)^2):", result)

#6
amt = int(input("enter amount:"))
rate = float(input("enter rate:"))
years = float(input("enter years:"))

future_value = amt * (1 + rate/100) ** years
print("Future Value:", round(future_value, 2))

#7
s = input("Enter a number: ")

print("Integer:", int(s))
print("Float:", float(s))

#8
n = int(input("Enter n: "))

total = n * (n + 1) // 2
print("Sum:", total)

#9
num = input("Enter a number: ")

nsum = 0
for i in num:
    nsum += int(i)

print("Sum of digits:", nsum)

#10
ch = input("Enter a character: ")

print("ASCII value:", ord(ch))

#11
s = input("enter a number:")

if s.isnumeric():
    print("string is numeric")
else:
    print("sring is not numeric")

#12
for i in range(5):
    print("***")

#13
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=" ")
#14
import math

C = 50
H = 30

values = input("Enter values: ").split(",")

result = []
for D in values:
    Q = math.sqrt((2 * C * int(D)) / H)
    result.append(str(round(Q)))

print(",".join(result))'''

#15

for i in range(5, 0, -1):
    print("*" * i)













 
