from BirthBook.Variables import Variables as v
from BirthBook.Maths import Maths as m
import keyboard as k


def show_menu():
    print('''
    1. Show birthday book.
    2. Add birthday.
    3. Change birthday.
    4. Delete birthday.
    5. Find birthday.
    d. Delete all data
    6. Exit. ''')


def main():
    choose = 0

    while choose != '6':
        show_menu()
        choose = input('Choose action: ')

        if choose == '1':
            m.print_birthday_book()
            k.press_and_release('enter', False, False)
            # input("Press 'Enter' to continue...")

        elif choose == '2':
            m.add_new_birthday(input('Input name: '), input('Input birthday: '))
            y_answer = input('Want to add more?')

            while y_answer in v.positive_answers:
                m.add_new_birthday(input('Input name: '), input('Input birthday: '))
                y_answer = input('Want to add more?')
            k.press_and_release('enter', False, False)

        elif choose == '3':
            m.change_birtday(
                input("Input name for change birthday: "),
                input("Type new birthday: "))
            input("Press 'Enter' to continue...")

        elif choose == '4':
            if m.delete_birthday(input("Input name for delete birthday: ")):
                y_answer = input('Want to delete more?')

                while y_answer in v.positive_answers:
                    m.delete_birthday(input('Input name for delete birthday: '))
                    y_answer = input('Want to delete more?')
            else:
                k.press_and_release('enter', False, False)

        elif choose == '5':
            m.find_birthday_by_name(input("Input Name for search: "))
            k.press_and_release('enter', False, False)

        elif choose == 'd':  # delete all
            print('After your accept - all data will be deleted')
            var_del = input('Input "DELETE" for delete: ')
            if var_del == "DELETE":
                m.delete_all_data()

        elif choose == '6':  # Exit
            exit(0)


# Run main
if __name__ == '__main__':
    main()
