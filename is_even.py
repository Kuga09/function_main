# Checking if a number is even


# Function for determining the parity of a number
def is_even(a):
    if a%2==0:
        return True
    else:
        return False

# Main function
def main():
    print('Введите введите число:')
    a=int(input())
    res = is_even(a)
    if res is True:
        print('Число',a,'четное')
    else:
        print('Число',a,'нечетное')


if __name__ == '__main__':
    main()