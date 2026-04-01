from models.student import Student
from presentation_layer.main_menu import MainMenu
from presentation_layer.menu import Menu, Validator


class NewStudentMenu(Menu):
    def render(self):
                print("""
===========================
New Student Menu
""")

                first_name: str = self.get_input("First name: ", Validator.NAME)
                last_name: str = self.get_input("Last name: ", Validator.NAME)
                major: str = self.get_input("Major: ")
                email = self.get_input("Email: ", Validator.EMAIL)
                year: str = self.get_input("Year: ")

                new_student: Student = Student(first_name, last_name, major, email, year)
                self.terminal.student_service.save(new_student)

                self.terminal.navigate(MainMenu(self.terminal))


# pass the function to navigate as a callback - no I don't think this helps
# instead of referencing the classes to navigate, have a set of enumerations

