num1 = input("choose your first number ")
op = str(input("choose 'd' for divide or 'm' for multiply or 'p' for plus or 's' for subtract"))
num2 = input("choose your second number ")

eq = num1 + op + num2

print("This is the equation you have come up with " + str(eq))

a = float(num1) + float(num2)
b = float(num1) / float(num2)
c = float(num1) * float(num2)
d = float(num1) - float(num2)


if op in ["d"]:
    print("Since you chose the operation /, your answer is ")
    print(b)


if op in ["m"]:
    print("Since you chose the operation *, your answer is ")
    print(c)


if op in ["p"]:
    print("Since you chose the operation +, your answer is ")
    print(a)


if op in ["s"]:
    print("Since you chose the operation -, your answer is ")
    print(d)
