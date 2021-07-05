import sqlite3

from CW3.Employee import Employee

class NonUniqueResultError(Exception): pass


class EmployeeRepository:
    def __init__(self, conn):
        self.conn = conn

    def find_by_id(self, id):
        return self.find_one('id', id)

    def find_by_name(self, name):
        return list(set(self.find_all('forename', name) + self.find_all('surname', name)))

    def find_one(self, property_name, property_value):
        result = self.find_all(property_name, property_value)
        if not isinstance(result, list):
            return result
        if len(result) > 1:
            raise NonUniqueResultError("Found {} records with {} {}".format(len(result), property_name, property_value))
        return result[0]

    def find_all(self, property_name, property_value):
        results = self.conn.cursor().execute(
            "SELECT id, title, forename, surname, email_address, salary"
            " FROM info WHERE {}=?".format(property_name), (property_value,)
        ).fetchall()

        if len(results) == 0:
            return None

        return [EmployeeEntity(self.conn, *result) for result in results]




class EmployeeEntity(Employee):

    def __init__(self, conn, employeeID=None, title=None, forename=None, surname=None, email=None, salary=None):
        super().__init__(employeeID, title, forename, surname, email, salary)
        self.conn = conn

    def update(self, property_name, property_value):
        self.conn.cursor().execute(
            "UPDATE info SET {}=? WHERE id=?".format(property_name),
            (property_value, self.get_employee_id())
        )
        self.conn.commit()

    def set_title(self, title):
        super().set_title(title)
        self.update('title', title)


#TODO: insert, delete (and use from the DBOperations function)
#TODO: update through setters
#TODO: update id through setters is special
