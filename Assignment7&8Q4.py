class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary
        raise TypeError("Operand must be an instance of Employee")

if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    
    print("Combined Salary : Rs", emp1 + emp2)
    print("Salary Difference : Rs", emp2 - emp1)
    print("Does Bob have a higher salary? \n", emp1 < emp2)
    print("Does Alice have a higher salary? \n", emp1 > emp2)
    print("Do they have the same salary? \n", emp1 == emp2)