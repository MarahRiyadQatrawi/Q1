number1 = float(input("The first number"))
print("1_+, 2_-, 3_*, 4_/, 5_^, 6_%")

import operator
operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod
}
do_what = input("Enter calculation symbols for calculation you want to perform: ")
number2 = float(input("The second number"))
result = "the output of operation"

if do_what == '+' or "1":
    result = number1 + number2
elif do_what == '-' or "2":
    result = number1 - number2
elif do_what == '*' or "3":
    result = number1 * number2
elif do_what == '/' or "4":
    result = number1 / number2
elif do_what == '**' or '5':
    result = number1 ** number2
elif do_what == '%' or '6':
    result = number1 % number2
print(result)

final_result = input("EX.choices: 1-Rounded the result, 2-Floor the result, 3-Exit: ")

if final_result == "1":
    print(round(result))
elif final_result == '2':
    print(int(result))
elif final_result == '3':
    print(result)

print(final_result)





