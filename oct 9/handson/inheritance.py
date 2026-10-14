class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_emp(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    pass

dev=Developer("Nab",200000)
dev.display_emp()
