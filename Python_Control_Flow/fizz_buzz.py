for q in range(1, 50):
    if (q % 3 == 0 and q % 5 == 0):
        print('fizzbuzz')
    elif (q % 3 == 0):
        print('Fizz')
    elif (q % 5 == 0):
        print('Buzz')
    else:
        print(q)