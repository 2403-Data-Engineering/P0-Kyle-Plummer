from dataclasses import dataclass


@dataclass
class Student:
    id: int
    first_name: str
    last_name: str
    major: str
    email: str
    year: str



# kyle = Student(id=None, first_name="Kyle", last_name="Plummer", major="CS", email="kyle.plummer@revature.com", year="Senior")
# kyle2 = Student(None, "Kyle", "Plummer", "CS", "kyle.plummer@revature.com", "Senior")
# print(kyle)
# print(kyle2)
# print(kyle.major)