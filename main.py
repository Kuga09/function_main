# Main file of the project


# import all nessesray libs and modules
import sum_digits as sd # import my own module
import temperature as temp # import my own module
import is_even as ev # import my own module

def main():
    user_choise = input('Выберите, что вы хотите сделать:\n'
                        '1 — Перевод температуры из Цельсии в Фаренгейты\n'
                        '2 — Подсчет суммы цифр числа\n'
                        '3 — Проверка числа на четность\n')
    if user_choise == '1':
        temp.main()
    elif user_choise == '2':
        sd.main()
    elif user_choise == '3':
        ev.main()
    else:
        main()
if __name__ == '__main__':
    main()