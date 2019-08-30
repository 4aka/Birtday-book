from BirthBook import variables as v
from ctypes.wintypes import PINT

class maths (object):
    
# Variables
    global name_symbols 
    name_symbols = v.vriables().name_symbols
    global birth_symbols 
    birth_symbols = v.vriables().birth_symbols

    
# data structure
    @staticmethod
    def view(name, birth):
        ln = len(list(name))   # name length
        
        if (name[0] in name_symbols):
            return print("~~~~~ Entry has forbidden symbol")
        elif (birth[0] in birth_symbols):
            return print("~~~~~ Entry has forbidden symbol")
        elif (len(list(name)) >= 30):
            return print("~~~~~ Name or date too long")
        else:
            print_string = name + (36 - ln)*' ' + birth + '\n'
            return print_string

    
# Print data. Using view
    @staticmethod
    def print_birthday_book():
        line = maths.view("Name:", "Birthday:")
        print(line)
        
        f = open(v.vriables.file, "r")
        array = [row.rstrip() for row in f]

        for i in range(len(array)):
            print(array[i])

    
# Add new birthday. Set Name and Date
    @staticmethod
    def add_new_birthday(name, birthday):
        string = maths.view(name, birthday)
        f = open(v.vriables.file, "a")
        f.write(string)
        f.close


# Delete string from list
    @staticmethod
    def delete_birthday():
        birth_list = []
        f = open(v.vriables.file, 'r')
        array = [row.rstrip() for row in f]
        
        for j in range(len(array)):
            s = (str(j) + ' ' + array[j])
            birth_list.append(s)
            print(birth_list[j])

        num = int(input('\n' + "Please set integer for delete..."))
        print("You choosed - " + str(num))

        if num in v.vriables.integers:
            print("1. Entry is incorrect. Try again.")
        elif num <= -1 and num >= (len(birth_list) + 1):
            print("2. Entry is incorrect. Try again.")
        else:
            birth_list.pop(num)
            f = open(v.vriables.file, 'w')
            for line in range(len(birth_list)):
                f.writelines(birth_list[line] + '\n')
            f.close()
            return True
        # TODO after deleting data viewing incorrect
    
    
# Clear data
    @staticmethod    
    def delete_all_data(var_del):
        if (var_del == "DELETE"):
            f = open(v.vriables.file, "w")
            f.write("")
            f.close
            print("Your data has deleted!")
            return True
        else:
            print("Your input is wrong, try again!")
            return False
        
    @staticmethod
    def change_birthday(name):
        print("soon")
        #TODO

#     def change_birthday(name):
#         self._birth_book[0][self.search_month(name)] = input("Input new name: ")
#         self._birth_book[1][self.search_month(name)] = input("Input new birthday: ")