num1=input("what is the first number? ")
op = input("What operation will you be using? ")
num2=input ("What is the second number? ")


if op == "+":
    total = int(num1) + int(num2)
elif op == "-":
     total = int(num1) - int(num2)
elif op == "*":
    total= int(num1) * int(num2)
elif op == "/":
    total= int(num1) / int(num2)


print(str(total))

