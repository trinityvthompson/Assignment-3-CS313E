"""
This module defines a set of classes for managing different types of
employees within a company.
"""

class Employee:
    """Represents a general employee."""
    def __init__(self, **kwargs):
        """
        Initializes an Employee object with given keyword arguments: 
        name, identifier, salary
        """
        self.name = kwargs.get("name", "None")
        self.identifier = kwargs.get("identifier", "None")
        self.salary = kwargs.get("salary", "None")

    def __str__(self):
        """Returns a string representation of the Employee object."""
        return f"Employee\n{self.name}, {self.identifier}, {self.salary}"


class PermanentEmployee(Employee):
    """Represents a Permanent Employee with benefits they can select from."""
    def __init__(self, **kwargs):
        """Initializes a permanent employee object."""
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits", [])

    def cal_salary(self):
        """Calculate salary based on benefits provided"""
        if "health_insurance" in self.benefits and "retirement" in self.benefits:
            return self.salary * 0.7
        if "health_insurance" in self.benefits:
            return self.salary * 0.9
        if "retirement" in self.benefits:
            return self.salary * 0.8
        #Return base salary if no benefits apply (none of the conditions are met)
        return self.salary

    def __str__(self):
        """Returns string representation of Permanent Employee object."""
        return f"PermanentEmployee\n{self.name}, {self.identifier}, {self.salary}, {self.benefits}"

class Manager(Employee):
    """Represents a manager, a special type of employee, with a bonus in addition to main salary."""
    def __init__(self, **kwargs):
        """Initializes a manager object."""
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus", 0)

    def cal_salary(self):
        """Calculates total salary including bonus"""
        return self.salary + self.bonus

    def __str__(self):
        """Returns string representation of Manager object."""
        return f"Manager\n{self.name}, {self.identifier}, {self.salary}, {self.bonus}"


class TemporaryEmployee(Employee):
    """Represents a temporary employee, an employee that gets paid per hour."""
    def __init__(self, **kwargs):
        """Initializes a temporary employee object."""
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours", 0)

    def cal_salary(self):
        """Calculates total salary based on hours worked and hourly wage."""
        return self.salary * self.hours

    def __str__(self):
        """Returns string representation of Temporary Employee object."""
        return f"TemporaryEmployee\n{self.name}, {self.identifier}, {self.salary}, {self.hours}"


class Consultant(TemporaryEmployee):
    """Represents a consultant, a temporary employee who also travels."""
    def __init__(self, **kwargs):
        """Initializes a consultant object."""
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel", 0)

    def cal_salary(self):
        """Calculates salary as temporary employee plus travel benefits."""
        return super().cal_salary() + (1000 * self.travel)

    def __str__(self):
        """Returns string representation of Consultant object."""
        return f"Consultant\n{self.name}, {self.identifier}, \
            {self.salary}, {self.hours}, {self.travel}"


class ConsultantManager(Consultant, Manager):
    """Represents a consultant who is also a manager."""
    def __init__(self,  **kwargs):
        """Initializes a consultant manager object."""
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    def cal_salary(self):
        """Calculates salary including bonus, hours worked, and travel pay."""
        return (Consultant.cal_salary(self)) + self.bonus

    def __str__(self):
        """Returns the string representation of Consultant Manager object."""
        return f"ConsultantManager\n{self.name}, {self.identifier}, \
                {self.salary}, {self.hours}, {self.bonus}, {self.travel}"

###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
