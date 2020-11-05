"""
class point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = point(2,8)
print(p.x)
print(p.y)
"""

"""
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)

"""


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = Flight(capacity=3)

people = ["Harry", "Ron", " Harmonie", "graphie"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")
"""

class Flight:

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(capacity=3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")
"""