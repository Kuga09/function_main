# Take temperature in Celcium from user
# and convert it to Farenheit

# Convertation function
def temperature(C):
    return C*1.8+32

# Main function
def main():
    user_temp = float(input('Введите температуру в градусах Цельсия:'))
    res_temp = temperature(user_temp)
    print('Температуру в градусах Фаренгейта =',res_temp)


if __name__ == '__main__':
    main()