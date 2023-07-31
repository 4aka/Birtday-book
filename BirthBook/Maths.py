from BirthBook.Variables import Variables
from multipledispatch import dispatch


class Maths:

    @staticmethod
    def build_map_from_file():
        # Read file
        f = open(Variables.file, "r")

        # Create empty dict
        my_dict = {}

        for line in f.readlines():
            # Split each line by ', '.
            # Create array with 2 elements
            # Add elements to dict
            my_dict[line.split(', ', 2)[0]] = line.split(', ', 2)[1]

        # close the file
        f.close()

        # return dict
        return my_dict

    # Print data. Using view
    @staticmethod
    def print_birthday_book():
        for key, value in Maths.build_map_from_file().items():
            print(key + ', ' + value)

    # Add new birthday. Set Name and Date
    @staticmethod
    def add_new_birthday(name, birthday):
        Maths.write_to_the_file(name, birthday)

    @staticmethod
    @dispatch(dict)
    def write_to_the_file(my_dict):
        f = open(Variables.file, "w")
        # Delete content
        f.write('')

        # Write dictionary to the file
        for k, v in my_dict.items():
            f.write(k + ', ' + v + '\n')

        f.close()

    @staticmethod
    @dispatch(str, str)
    def write_to_the_file(name, birthday):
        # Open file for writing
        f = open(Variables.file, "a")
        f.write(name + ', ' + birthday + '\n')
        f.close()

    # Delete birthday from the list
    @staticmethod
    def delete_birthday(name):
        my_dict = Maths.build_map_from_file()
        Maths.print_birthday_book()

        # Delete birthday by name
        for k, v in my_dict.items():
            if k == name:
                my_dict.pop(name)

        # Print birthday book
        Maths.print_birthday_book()
        return True

    # Clear data
    @staticmethod
    def delete_all_data():
        f = open(Variables.file, "w")
        f.write("")
        f.close()
        print("The data has fully deleted!")

    @staticmethod
    def find_birthday_by_name(name):
        my_dict = Maths.build_map_from_file()

        # Change birthday by name
        for k, v in my_dict.items():
            if k == name:
                print(name + ' ' + my_dict[name])

    @staticmethod
    def change_birtday(name, birthday):
        my_dict = Maths.build_map_from_file()

        # Change birthday by name
        for k, v in my_dict.items():
            if k == name:
                my_dict[name] = birthday

        # Update birtday book
        Maths.write_to_the_file(my_dict)

        # Print birthday book
        Maths.print_birthday_book()
