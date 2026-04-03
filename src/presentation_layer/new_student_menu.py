from models.student import Student
from presentation_layer.main_menu import MainMenu
from presentation_layer.base_menu import BaseMenu, Validator


class NewStudentMenu(BaseMenu):
    def render(self):
                print("""
===========================
New Student Menu
""")

                first_name: str = self.get_input("First name: ", Validator.NAME)
                last_name: str = self.get_input("Last name: ", Validator.NAME)
                major: str = self.get_input("Major: ")
                email: str = self.get_input("Email: ", Validator.EMAIL)
                year: str = self.get_input("Year: ")

                print("DEBUG: ", first_name, last_name, major, email, year)


                new_student: Student = Student(None, first_name, last_name, major, email, year)
                self.terminal.student_service.save(new_student)

                self.terminal.navigate("main_menu")
                

# pass the function to navigate as a callback - no I don't think this helps
# instead of referencing the classes to navigate, have a set of enumerations

