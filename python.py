print("PLEASE, I BEG OF YOU, FOLLOW THE DIRECTIONS. THEY ARE FAIRLY SIMPLE")
num1 = input("choose your first number ")
op = str(input("choose 'd' for divide or 'm' for multiply or 'p' for plus or 's' for subtract"))
num2 = input("choose your second number ")


eq = num1 + op + num2

a = float(num1) + float(num2)
b = float(num1) / float(num2)
c = float(num1) * float(num2)
d = float(num1) - float(num2)


if op in ["d" ,  "D"]:
    print("Since you chose the operation /, your answer is ")
    print(b)


elif op in ["m" , "M"]:
    print("Since you chose the operation *, your answer is ")
    print(c)


elif op in ["p" , "P"]:
    print("Since you chose the operation +, your answer is ")
    print(a)


elif op in ["s" , "S"]:
    print("Since you chose the operation -, your answer is ")
    print(d)

else:
    print("FOLLOW THE DIRECTIONS")

