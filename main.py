def fizz_buzz(max_value):
  for number in range(1, max_value + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

    
fizz_buzz(100)
