# from M1.list_49_键盘操作 import mouse_move

# mouse_move()

###package测试成功

# class Employee(object):
#     pass

# employee1 = Employee()
# employee1.first = 'Harry'
# employee1.surname = 'Portter'
# employee1.salary = 4000
# employee1.email = 'Harry@163.com'
# print('{}, {}, {}'.format(employee1.first+'' +employee1.surname, employee1.salary, employee1.email))

class Employee():

    raiseAmount = 2
    employeeNum = 0
    def  __init__(self, first, surname, salary):
        self.first = first
        self.surname = surname
        self.salary = salary
        self.email = self.first + '.' + self.surname + '@163.com'
        Employee.employeeNum += 1
    
    @property
    def first(self):
        return self.__first
    
    @first.setter
    def first(self, value):
        if isinstance(value, str):
            self.__first = value
        else:
            print('please input a string')
    
    def infoSummary(self):
        return'{}, {}, {}'.format(self.first+'' + self.surname, self.salary, self.email)

    def raiseSalary(self):
        self.salary = self.salary*Employee.raiseAmount
    
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount
    
    @classmethod
    def newFromString(cls, empstr):
        first, surname, salary = empstr.split('-')
        return cls(first, surname, salary)
    
    @staticmethod
    def whatDay(day):
        num = day.weekday()
        if num == 0:
            print('Are you OK?')
        else:
            print('meishi')

class Writer(Employee):
    def __init__(self, first, surname, salary, masterwork):
        Employee.__init__(self,first,surname,salary)
        self.masterwork = masterwork

class Leader(Employee):
    def __init__(self, first, surname, salary, employees =None):
        super().__init__(first, surname, salary)
        ###?????
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
employee1 = Employee('Harry', 'Potter', 4000)
employee2 = Employee('bilbo', 'baggins', 4000)

# print(employee1.infoSummary(),employee2.infoSummary())
# employee1.raiseSalary()
# print(employee1.infoSummary(), Employee.raiseAmount)
# print(employee1.__dict__)
# print(employee1.__dict__['first'])
# Employee.setRaiseAmount(4)
# employee1.raiseSalary()
# print(employee1.infoSummary(), Employee.raiseAmount)
# print(Employee.employeeNum)

empStr1 = 'J.K-Rowling-10000'
empStr2 = 'J.R.R-Tolkin-8000'

employee3 = Employee.newFromString(empStr1)
employee4 = Employee.newFromString(empStr2)
print(employee3.infoSummary() ,employee4.infoSummary())

# from datetime import date

# day = date.today()
# Employee.whatDay(day)
# print(help(Employee))
print('----------------------')
empWriter1 = Writer('Mark','Twain',8000,'worker')
print(empWriter1.infoSummary())

empLeader = Leader('Jstin','caesar',12000,[employee3,employee4])  
# print(empLeader.__dict__['employees'][0].__dict__['__first'])
employee3.first= 'BOB'
print(employee3.infoSummary())
# print(empLeader.__dict__['employees'][0].__dict__['__first'])
print(employee3.first)