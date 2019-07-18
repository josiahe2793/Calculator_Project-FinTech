num1=input("what is the first number? \n")
op = input("What operation will you be using? \n")
num2=input ("What is the second number? \n")

total = 0
if op.lower() == "+" or op.lower() == "add" or op.lower() == "addition" or op.lower() =="plus":
    total = int(num1) + int(num2)
    sym = "+"
    
elif op.lower() == "-" or op.lower() == "subtract" or op.lower() == "minus":
     total = int(num1) - int(num2)
     sym = "-"
     
elif op.lower() == "*" or op.lower() == "multiply" or op.lower() == "multiplication":
    total= int(num1) * int(num2)
    sym = "*"
    
elif op.lower() == "/" or op.lower() == "divide" or op.lower() == "division":
    total= int(num1) / int(num2)
    sym = "/"
    
    
print(str(num1) + " " + str(sym) + " " + str(num2) +  " = "  + str(total))

