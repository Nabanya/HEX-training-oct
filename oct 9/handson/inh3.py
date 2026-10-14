class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_emp(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language

dev=Developer("Nivi",90000,"Python")

print(dev.name)
print(dev.salary)
print(dev.language)