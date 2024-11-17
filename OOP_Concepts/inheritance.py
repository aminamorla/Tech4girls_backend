class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        print(f'Name: {self.name}')
        print(f'position: {self.position}')
#child class manager inheriting from employee
class Manager(Employee):
    def __init__(self, name, position, department):
        #initialize the parent class attributes using super()
        super().__init__(name, position)
        self.department = department
    #overide the get_details method
    def get_details(self):
        super().get_details() #call the parent class method
        print(f'department: {self.department}')
#demonstrate creating instances and calling get_details()
employee = Employee('Amina', 'Software Enginner')
manager = Manager('Abass', 'Preject Manager', 'Development')
#display details for employee
print('Employee Details:')
employee.get_details()
print()

#display details for manager
print('Manager Details:')
manager.get_details()
print()