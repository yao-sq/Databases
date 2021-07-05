import sqlite3
from CW3.Employee import Employee
from CW3.EmployeeRepository import EmployeeRepository, EmployeeEntity


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

    def get_connection(self):
        self.conn = sqlite3.connect('store')
        return self.conn

    def create_table(self):
        try:
            self.conn = self.get_connection()
            self.conn.execute(
                "CREATE TABLE 'info' (id INT UNSIGNED PRIMARY KEY,title VARCHAR(20), forename VARCHAR(20), surname VARCHAR(20), email_address VARCHAR(50), salary INT UNSIGNED)")
            print("Create table: Table created successfully")
        except:
            print("Warning: This table is already created")
            # raise

    def insert_data(self):
        self.conn = self.get_connection()

        try:
            emp = Employee()
            # id is not an actual column in the table
            emp.set_employee_id(int(input("Enter Employee ID: ")))
            emp.set_title(str(input("Enter Title: ")))
            emp.set_forename(str(input("Enter Forename: ")))
            emp.set_surname(str(input("Enter Surname: ")))
            emp.set_email_address(str(input("Enter Email: ")))
            emp.set_salary(str(input("Enter Salary: ")))

            print(tuple(str(emp).split("\n")))
            self.conn.cursor().execute(
                "INSERT INTO info"
                " (id, title, forename, surname, email_address, salary)"
                " VALUES (?, ?, ?, ?, ?, ?)",
                (emp.employeeID, emp.title, emp.forename, emp.surname, emp.email, emp.salary)
            )
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print("The id you just typed is a duplicate of existing id, please try again", e)

    def report_data(self):
        print("---Report data:---")
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

    def delete_all_data(self):
        self.conn = self.get_connection()

        self.conn.execute("DELETE FROM info")
        self.conn.commit()

    def search_data(self, search_id=None):
        is_present = False
        self.conn = self.get_connection()

        if search_id is None:
            console_input = input("Enter Employee ID for search: ")
            try:
                search_id = int(console_input)
            except:
                print("Wrong type, ID should be int")
                return False
        else:
            if type(search_id) != type(int()):
                print("search_id provided should be int")
                return False

        self.cur = self.conn.cursor()
        result_all = self.cur.execute("SELECT * FROM info WHERE id=?", (search_id,)).fetchall()
        result_one = self.cur.execute("SELECT * FROM info WHERE id= {}".format(search_id)).fetchone()

        if type(result_one) != type(tuple()):
            print("No record")
        else:
            is_present = True
            for row in result_all:
                print(row)
                # print("id= ", row[0])
                # print("title = ", row[1])
                # print("forename = ", row[2])
                # print("surname = ", row[3])
                # print("email_address = ", row[4])
                # print("salary = ", row[5])

        return is_present

    def delete_data(self):
        self.conn = self.get_connection()

        console_input = input("Enter Employee ID to delete: ")
        try:
            delete_id = int(console_input)
        except:
            print("Wrong type, ID should be int")
            return False

        ### Search for data by id and then delete the whole row
        if self.search_data(delete_id):
            self.conn.execute("DELETE FROM info WHERE id = {}".format(delete_id))
            self.conn.commit()

        ### How about delete just a cell?
        # and fill in null for the deleted cell?
        # maybe in another function?

    def update_data(self):
        self.conn = self.get_connection()
        console_input = input("Enter Employee ID to update: \n")
        try:
            update_id = int(console_input)
        except:
            print("Wrong type, ID should be int")
            return False

        ### update cell FIXME: if the id is set to be a string, it can't be changed back
        update_col = str(input("Enter the column name: \n"))
        update_content = str(input("Enter the content to be updated: \n"))
        query = "UPDATE info SET {} = '{}' WHERE id= '{}'".format(update_col, update_content, update_id)
        print(query)
        if self.search_data(update_id):
            self.conn.execute(query)
            self.conn.commit()


        ###  alter table: add column
        ###  alter table: drop column
        ###  alter table: alter/modify column



if __name__ == '__main__':
    db_ops = DBOperations()
    # db_ops.create_table()
    # db_ops.delete_all_data()
    # db_ops.insert_data()
    # db_ops.search_data()
    # db_ops.delete_data()
    # db_ops.update_data()
    # db_ops.report_data()

    conn = db_ops.get_connection()
    repo = EmployeeRepository(conn)

    # employee = repo.find_by_id(127)
    # if employee:
    #     print(employee)
    #     employee.set_title(input("New title: "))
    # else:
    #     print("No result with this id")
    #
    # print("---By name---")
    # print([str(s) for s in repo.find_by_name("Yao")])

    # emp = Employee(3, 'Dr', 'Sleep', 'Moore', 'mm', 500)
    # repo.insert(emp)

    # repo.delete(500)

    emp = repo.find_by_id(3)
    emp.set_employee_id(100)

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
