state1= "Welcome to the Calculator Program!"
state2 = "This program accepts the following operations: \n                    '+' , '-', '*', '/', '^' and '%' aka division remainer"
wel = state1.center(100)
this = state2.center(170)
print(wel)
print(this)
answer = input("Would you like to calculate? ")


while answer.lower() == "yes":
    
    num1=input("What is the first number? \n")
    op = input("What operation will you be using? \n")
    num2=input ("What is the second number? \n")
    total = 0
    
    
    
    if op.lower() == "+" or op.lower() == "add" or op.lower() == "addition" or op.lower() =="plus":
        total = float(num1) + float(num2)
        sym = "+"
        
    elif op.lower() == "-" or op.lower() == "subtract" or op.lower() == "minus":
         total = float(num1) - float(num2)
         sym = "-"
         
    elif op.lower() == "*" or op.lower() == "multiply" or op.lower() == "multiplication":
        total= float(num1) * float(num2)
        sym = "*"
        
    elif op.lower() == "/" or op.lower() == "divide" or op.lower() == "division":
        total= float(num1) / float(num2)
        sym = "/"
    
    elif op.lower() == "**" or op.lower() == "power" or op.lower() == "^":
        total= int(num1) ** int(num2)
        sym = "**"
    
    elif op.lower() == "%" or op.lower() == "remainder" or op.lower() == "left over":
        total= int(num1) % int(num2)
        sym = "%"
    else:
        print("You messed up we are going to assume you meant addition!")
        total = float(num1) + float(num2)
        sym = "+"
    print(str(num1) + " " + str(sym) + " " + str(num2) +  " = "  + str(total))
    
    statement=" Is That All The Math, You Got For Me? I Can Do Almost Anything Buddy! "
    Is = statement.center(50)
    print(Is)
    answer = input("Would you like to calculate again? \n")
    if answer.lower() == "yes" or answer.lower() == "y" :
        answer.lower() == "yes"
    else: 
        print("Have a good day!")
