class Employee:
    def work(self):
        print("Employee is working.")

class Developer(Employee):
    def code(self):
        print("Writing Python code")

class Tester(Employee):
    def test(self):
        print("Testing application")

emp=Employee()
emp.work()

dev=Developer()
dev.work()
dev.code()

test=Tester()
test.work()
test.test()
