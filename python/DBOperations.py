import sqlite3

from python.Employee import Employee


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
        self.conn = self.get_connection()
        self.conn.execute("DROP TABLE IF EXISTS info")
        self.conn.execute("CREATE TABLE 'info' (id INT UNSIGNED,"
                     "                     title VARCHAR(20), "
                     "                     forename VARCHAR(20), "
                     "                     surname VARCHAR(20), "
                     "                     email_address VARCHAR(50), "
                     "                     salary INT UNSIGNED)")
        print("Init step: Table created successfully")

    def get_connection(self):
        self.conn = sqlite3.connect('store')
        print("Database has been created")
        return self.conn

    def create_table(self):
        try:
            self.conn = self.get_connection()
            self.conn.execute("CREATE TABLE 'info' (id INT UNSIGNED,title VARCHAR(20), forename VARCHAR(20), surname VARCHAR(20), email_address VARCHAR(50), salary INT UNSIGNED)")
            print("Create table: Table created successfully")
        except:
            print("Create table: This table is already created")
            raise

    def insert_data(self):
        self.conn = self.get_connection()

        emp = Employee()
        #id is not an actual column in the table
        emp.set_employee_id(int(input("Enter Employee ID: ")))

        title = str(input("Enter Title: "))
        emp.set_title(title)

        emp.set_forename(str(input("Enter Forename: ")))
        emp.set_surname(str(input("Enter Surname: ")))
        emp.set_email(str(input("Enter Email: ")))
        emp.set_salary(str(input("Enter Salary: ")))

        print(tuple(str(emp).split("\n")))
        self.conn.cursor().execute("INSERT INTO info VALUES {}".format(tuple(str(emp).split("\n"))))
        self.conn.commit()
        print("Insert data: new data has been inserted")

    def report_data(self):
        self.conn = self.get_connection()

        cursor = self.conn.execute("SELECT id, title,forename,surname,email_address, salary from info")

        for row in cursor:
            print(row)
            # print("id= ", row[0])
            # print("title = ", row[1])
            # print("forename = ", row[2])
            # print("surname = ", row[3])
            # print("email_address = ", row[4])
            # print("salary = ", row[5])

if __name__ == '__main__':
    db_ops = DBOperations()
    # db_ops.create_table()

    db_ops.insert_data()
    db_ops.report_data()


    # while True:
    #     print("\n Menu:")
    #     print("******************")
    #     print(" 1. Create table")
    #     print(" 2. Insert data")
    #     print(" 3. Update data ")
    #     print(" 4. Delete data")
    #     print(" 5. Search data")
    #     print(" 6. Report data")
    #     print(" 7. Exit menu")
    #
    #     choice = str(input("Enter your choice: \n"))
    #     if choice == '1':
    #         pass
    #     elif choice == '2':
    #         pass
    #     elif choice == '3':
    #         pass
    #     elif choice == '4':
    #         pass
    #     elif choice == '5':
    #         pass
    #     elif choice == '6':
    #         pass
    #     elif choice =='7':
    #         exit(0)
    #     else:
    #         print("Invalid choice")



