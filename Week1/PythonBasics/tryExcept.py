try:
    number=int(input("Enter number: "))
    print(number)
except ValueError as e:
    print(e) 