from art import logo

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
  print(logo)
  
  num1 = float(input("Digite o primeiro numero: "))

  for symbol in operations:
    print(symbol)
  calculate = True

  while calculate:
    operation_symbol = input("Escolha uma operação: ")
    num2 = float(input("Digite o proximo numero: "))
    calculation = operations[operation_symbol]
    result = calculation(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to exit: ")
    if choice == 'y':
      num1 = result
    else:
      calculate = False
      calculator()

calculator()