# Counting the sum of the digits of a number


# Counting function
def sum_digits(a):
    sum=0
    for i in range(0,len(a)):
        sum+=int(a[i])
    return sum

# Main function
def main():
    print('Введите число:')
    a=input()
    print('Сумма всех цифр числа',a,'=', sum_digits(a))


if __name__ == '__main__':
    main()