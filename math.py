from BirthBook import variables as v

class maths (object):
    
# Variables
    global name_symbols 
    name_symbols = v.vriables().name_symbols
    global birth_symbols 
    birth_symbols = v.vriables().birth_symbols

    
# data list structure
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
        i = 0
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
        f = open(v.vriables.file, 'r')
        array = [row.rstrip() for row in f]
        i = 0
        for i in range(len(array)):
            print(str(i) + '  ' + array[i])

        num = input('\n' + "Please set integer that you want delete...")
        if num not in v.vriables.integers:
            print("There are not such integer.")
        else:
            output = []
            for line in f:
                if not num in line[0]:
                    output.append(line)
            f.close()
            
            f = open(v.vriables.file, 'w')
            f.writelines(output)
            f.close()
    
    
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