largest = None
smallest = None

while True:
    user_input = input("Enter an integer number or 'done' to finish: ")

    if user_input == 'done':
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

if largest is not None:
    print("Maximum is", largest)

if smallest is not None:
    print("Minimum is", smallest)
