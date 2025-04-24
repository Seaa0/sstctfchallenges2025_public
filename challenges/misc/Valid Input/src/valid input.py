flag = 'sstctf{isnum3ric()_4ls0_r3turn5_Tru3_for_n0n_4rab1c_num3ral5_so_u53_isd1gi+()}'

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