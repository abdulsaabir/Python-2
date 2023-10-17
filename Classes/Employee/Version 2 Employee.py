# Define a class called Employee
class Employee:
    # Constructor method (__init__) is called when an instance is created
    # The 'self' parameter represents the instance itself
    def __init__(self, first, last, pay):
        # Assign values to instance attributes
        self.firstName = first
        self.lastName = last
        self.pay = pay
        # Combine first name, last name, and made from it an email address
        self.email = self.firstName + self.lastName + '@gmail.com'
    
    # Define a method within the class to get the full name of an employee
    def fullname(self):
        return f'{self.firstName} {self.lastName}'

# Create an instance (object) of the Employee class and pass values to the constructor
emp1 = Employee('ahmed', 'ciise', 4000)

# Access and print attributes of the emp1 instance
print(emp1.firstName)
print(emp1.lastName)
print(emp1.email)
print(emp1.pay)

# Create another instance (object) of the Employee class with different values
emp2 = Employee('falastiin', 'ahmed', 5000)

# Access and print attributes of the emp2 instance
print(emp2.firstName)
print(emp2.lastName)
print(emp2.email)
print(emp2.pay)
