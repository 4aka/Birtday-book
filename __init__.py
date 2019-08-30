from BirthBook.variables import vriables as v
from BirthBook.math import maths as m
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
            input("Press 'Enter' to continue...")
        
            
        elif choose == '2':
            name = input('Input name: ')
            birthday = input('Input birthday: ')
            m.add_new_birthday(name, birthday)
            y_answer =  input('Want to add more?')
            while (y_answer in v.right_list):
                name = input('Input name: ')
                birthday = input('Input birthday: ')
                m.add_new_birthday(name, birthday)
                y_answer =  input('Want to add more?')
            k.press_and_release('enter', False, False)
        
            
        elif choose == '3':
            m.change_birthday(input("Input ID for change birthday: "))
            input("Press 'Enter' to continue...")
        
        
        elif choose == '4':
            answer = m.delete_birthday()
            if answer:
                y_answer =  input('Want to delete more?')
                while (y_answer in v.right_list):
                    name = input('Input integer for delete: ')
                    m.delete_birthday()
                    y_answer =  input('Want to delete more?')
            else:
                print("fail")
            k.press_and_release('enter', False, False)
        
            
        elif choose == '5':
            m().print_birthday(input("Input Name for search: "))
            input("Press 'Enter' to continue...")
            
        
        elif choose == 'd':     # delete all
            print('After your accept - all data will has deleted')
            var_del = input('Input "DELETE" for delete: ')
            var_bool = m.delete_all_data(var_del)
            if var_bool == True:
                input("Press 'Enter' to continue...")
            else:
                var_del = input('Input "DELETE" for delete: ')
                var_bool = m.delete_all_data(var_del)
        
                
        elif choose == '6':     # Exit
            exit(0)


# Run main
if __name__ == '__main__':
    main()