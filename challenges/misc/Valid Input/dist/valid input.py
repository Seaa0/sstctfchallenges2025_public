flag = 'sstctf{REDACTED}'

number = input('Enter a number: ')
if number.isnumeric():
    try:
        number = int(number)
        print(number)
    except ValueError:
        print('Why are you such a bad user?')
        print(flag)
else:
    print('Input validation failed!')