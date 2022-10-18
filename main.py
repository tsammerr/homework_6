try:
    num = int(input('number -> '))

    if num > 0 and num !=7:
        print('Number is positive')

    if num < 0:
        print('Number is negative')


    if num == 0:
        print('Number is equal to zero')

    if num == 7:
            print('Good bye!')

except Exception as ex:
    print(ex)