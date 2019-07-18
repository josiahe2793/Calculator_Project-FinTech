num1=input("what is the first number? ")
op = input("What operation will you be using? ")
num2=input ("What is the second number? ")


if op == "+" or "add" or "addition" or "plus":
    total = int(num1) + int(num2)
    sym = "+"
elif op == "-" or "subtract" or "minus":
     total = int(num1) - int(num2)
     sym = "-"
elif op == "*" or "multiply" or "multiplication":
    total= int(num1) * int(num2)
    sym = "*"
elif op == "/" or "divide" or "division":
    total= int(num1) / int(num2)
    sym = "/"


print(str(num1) + " " + sym + " "+ str(num2) +  " = "  + str(total))

