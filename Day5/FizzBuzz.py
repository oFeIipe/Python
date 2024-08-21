for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: #confere se algum número e divisivel por 3 e 5
        print("FizzBuzz")
    elif number % 3 == 0: #confere se o número é divisivel por 3
        print("Fizz")
    elif number % 5 == 0: #confere se o número é divisivel por 5 
        print("Buzz")
    else:
        print(number) #printa os números restantes

      
     