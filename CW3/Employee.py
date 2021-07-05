class Employee:
    def __init__(self, employeeID = None, title = None, forename = None, surname = None, email = None, salary = None):
        self.employeeID = employeeID
        self.title = title
        self.forename = forename
        self.surname = surname
        self.email = email
        self.salary = salary

    def set_employee_id(self, id):
        self.employeeID = id

    def set_title(self, title):
        self.title = title

    def set_forename(self, forename):
        self.forename = forename

    def set_surname(self, surname):
        self.surname = surname

    def set_email_address(self, email):
        self.email = email

    def set_salary(self, salary):
        self.salary = salary

    def get_employee_id(self):
        return self.employeeID

    def get_title(self):
        return self.title

    def get_forename(self):
        return self.forename

    def get_surname(self):
        return self.surname

    def get_email_address(self):
        return self.email

    def get_salary(self):
        return self.salary

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Employee) and self.employeeID == o.employeeID

    def __hash__(self) -> int:
        return hash(self.employeeID)

    def __str__(self):
        return ",".join((
            str(self.employeeID),
            self.title,
            self.forename,
            self.surname,
            self.email,
            str(self.salary)
        ))

