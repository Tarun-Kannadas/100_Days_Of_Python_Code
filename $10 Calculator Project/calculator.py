import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division,
}

def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("Enter your first Number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        action = input("Pick an Operation: ")
        num2 = float(input("Enter next Number: "))
        result = operations[action](num1,num2)
        print(f"{num1} {action} {num2} = {result}")

        option = input(f"Type 'y' to continue with {result} or Type 'n' to start a new calculation: ").lower()

        if option == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()