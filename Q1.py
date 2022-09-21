name = input("your name:")
age = int(input("your age:"))
address = input("your address:")

text = "Hello Mr/Ms" ,name, "age",age,"located in",address, ". thanks for beeing one of our community, Enjoy."

condition = name.isalpha()
if condition is True:
    print(text)
elif age != "" and address != "":
    print(text)
else:print("false")
