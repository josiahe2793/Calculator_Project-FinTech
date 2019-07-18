num1=input("what is the first number? \n")
op = input("What operation will you be using? \n")
num2=input ("What is the second number? \n")


if op == "+" or op == "add" or op == "addition" or op =="plus":
    total = int(num1) + int(num2)
    sym = "+"
elif op == "-" or op == "subtract" or op == "minus":
     total = int(num1) - int(num2)
     sym = "-"
elif op == "*" or op == "multiply" or op == "multiplication":
    total= int(num1) * int(num2)
    sym = "*"
elif op == "/" or op == "divide" or op == "division":
    total= int(num1) / int(num2)
    sym = "/"


print(str(num1) + " " + sym + " "+ str(num2) +  " = "  + str(total))

