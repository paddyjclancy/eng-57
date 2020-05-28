
def check_if_div3(num):
    return num % 3 == 0

def check_if_div5(num):
    return num % 5 == 0

def fizz_buzz_print_check(num):
    if check_if_div5(num) and check_if_div3(num):
        print("It is divisible by both 3 and 5")
    elif check_if_div5(num):
        print("Divisible by 5")
    elif check_if_div3(num):
        print("Divisible by 3")
    else:
        print(num)


while True:
    num = input("Provide a number, to check if divisible by 3, 5, or both   ")
    if 'exit' in num:
        print('Break')
        break

    if num.isnumeric():
        num = int(num)

    for number in range(1, num + 1):
        fizz_buzz_print_check(number)


def check_if_digit_div_num(digit, num_div):
    if digit % num_div == 0:
        return True
    else:
        return False

def bizzbuzz(num1, num2, number):
    for digit in range(1, (int(number) + 1)):
        if check_if_digit_div_num(digit, num1) and check_if_digit_div_num(digit, num2):
            print('bizzzzuu')
        elif check_if_digit_div_num(digit, num2):
            print('zzuu')
        elif check_if_digit_div_num(digit, num1):
            print('bizz')
        else:
            print(digit)


# start = input('Are you ready to play BIZZBUZZ? (Y/N) ')
# while True:
#     if start.upper() == 'N':
#         print('Maybe next time...')
#         break
#
#     elif start.upper() == 'Y':
#         number = input('Please enter number: ')
#         if number == 'penpinapplespen':
#             break
#         bizz = int(input('Choose your BIZZ: '))
#         buzz = int(input('Choose your ZZUU: '))
#         bizzbuzz(bizz, buzz, number)
#
#     else:
#         print("It's a Yes or No question.")
#         start = input('Are you ready to play BIZZBUZZ? >>(Y/N)<< ')

