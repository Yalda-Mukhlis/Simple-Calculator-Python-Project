from art import logo

def calculator():
    print(logo)
    print("Welcome to the Python Calculator 🧮")

    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
    }

    num1 = float(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        user_choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()

        if user_choice == "y":
            num1 = answer
        elif user_choice == "n":
            should_continue = False
            print("\n" * 50)
            calculator()
        else:
            print("Invalid input! Please type 'y' or 'n'.")
            should_continue = False


calculator()