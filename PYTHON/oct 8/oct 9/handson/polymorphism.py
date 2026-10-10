# class Developer:
#     def work(self):
#         print("Developer writes code")
#
# class Tester:
#     def work(self):
#         print("Tester tests the application")
#
# d1=Developer()
# t1=Tester()
#
# d1.work()
# t1.work()

class Developer:
    def work(self):
        print("Developer writes code")

class Tester:
    def work(self):
        print("Tester tests the application")

def perform_work(emp):
    emp.work()
    
d1=Developer()
t1=Tester()
# passing arg as objects
perform_work(d1)
perform_work(t1)