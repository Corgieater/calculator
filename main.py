from logo import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)
print("This is a calculator")


def calculating():
    num1 = float(input("Type a number\n"))

    end_of_calculating = False
    while end_of_calculating is not True:
        symbol = ""
        while symbol not in operations:   # Preventing invalid operation
            print("Invalid operation")
            symbol = input("Type an operation +, -, *, /\n")

        num2 = float(input("Type another number\n"))

        ans = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {ans}")
        keep_calculating = input(
            f"Do you wanna keep calculating with {ans}? press 'y'"
            f"\nor type 'n' to quit \n'new' to start a new one\n").lower()

        if keep_calculating == "n":
            print("Calculator out")
            end_of_calculating = True
        elif keep_calculating == "new":
            end_of_calculating = True  # to end the old calculating()
            calculating()  # start a new one
        else:
            num1 = ans


try:
    calculating()
except Exception as e:
    print(e)
