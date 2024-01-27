# employee class code in Python
# class definition

class Employee:

    # data member to count the number of Employees
    count_of_employees = 0
    __name=""
    __family=""
    __salary=0
    __department=""

    # function to set data 
    # constructor to intiliaze the name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.__name = name
        self.__family = family
        self.salary = salary
        self.__department = department
        Employee.count_of_employees += 1 #to count number of employees

    #function to calculate the average salary of an employee
    def average_salary(employees):
        total = 0
        for employee in employees:
            total += employee.salary
        return total / Employee.count_of_employees
    
    #displaying the details of an employee
    def showData(self):
        print("The count of an employee is\t\t:",Employee.count_of_employees)
        #print("The Name of an employee is\t:", self.__name)
        #print("The Family of an employee is\t:", self.__family)
        #print("The Department of an employee is\t:", self.__department)
        #print("The Salary of an employee is\t:", self.__salary)

#A subclass which is inherited the properties of the class
class FulltimeEmployee(Employee):
   #intiliazation
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)


#main class
def main():
    employees = []
    one = FulltimeEmployee("suneel", "katikareddy", 250000, "software-engineer")  #Declaration
    employees.append(one)  #appending
    two = FulltimeEmployee("ajay", "katikareddy", 160500, "civil-Enginer")
    employees.append(two)
    three = Employee("madhu", "suri", 189500, "Accountant")
    employees.append(three)
    four = Employee("ramesh", "adhani", 165400, "doctor")
    employees.append(four)
    Employee.showData(employees)  #showing the data of an employee
    print("Average salary of an employee is:", FulltimeEmployee.average_salary(employees)) #Average salary of an employee


if __name__ == "__main__":
    main()