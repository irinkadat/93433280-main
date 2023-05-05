names = []
while True:
    try:
        name = input('enter name:')
    except EOFError:
        break

    names.append(name)


if len(names)>2:
    print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")
elif len(names)==2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif len(names)==1:
    print(f"Adieu, adieu, to {names[0]}")
else:
    print('you should enter name!')


# second option using inflect module:

# import inflect

# p = inflect.engine()
# names = []

# while True:
#     try:
#         _names = input("Enter a name (or press Ctrl + D to exit): ").title()

#         names.append(_names)

#     except (KeyboardInterrupt, EOFError):
#         break

# if names:
#     res = f"Adieu, adieu, to {p.join(names)}."
#     print(res)
# else:
#     print("No names were entered.")