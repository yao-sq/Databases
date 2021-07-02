import sqlite3


class DBOperations:
    sql_create_table_firsttime = ""
    sql_create_table = ""

    sql_insert = ""
    sql_select_all = ""
    sql_search = ""
    sql_update = ""
    sql_delete = ""
    sql_drop_table = ""

    def __init__(self):
        pass

    def get_connection(self):
        conn = sqlite3.connect('store')
        print("Database has been created")

    def create_table(self):
        pass


if __name__ == '__main__':
    while True:
        print("\n Menu:")
        print("******************")
        print(" 1. Create table")
        print(" 2. Insert data")
        print(" 3. Update data ")
        print(" 4. Delete data")
        print(" 5. Search data")
        print(" 6. Report data")
        print(" 7. Exit menu")

        choice = str(input("Enter your choice: \n"))
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice =='7':
            exit(0)
        else:
            print("Invalid choice")



