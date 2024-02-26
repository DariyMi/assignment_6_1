import argparse


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2


parser = argparse.ArgumentParser()
parser.add_argument("num1", type=float)
parser.add_argument("operation", choices=["+", "-", "*", "/"])
parser.add_argument("num2", type=float)
args = parser.parse_args()

if args.operation == "+":
    result = add(args.num1, args.num2)
    print(f"{args.num1} + {args.num2} = {result}")
elif args.operation == "-":
    result = subtract(args.num1, args.num2)
    print(f"{args.num1} - {args.num2} = {result}")
elif args.operation == "*":
    result = multiply(args.num1, args.num2)
    print(f"{args.num1} * {args.num2} = {result}")
elif args.operation == "/":
    result = divide(args.num1, args.num2)
    print(f"{args.num1}  {args.num2} = {result}")
