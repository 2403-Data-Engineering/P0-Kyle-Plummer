from presentation_layer.base_terminal import BaseTerminal
from presentation_layer.main_menu import MainMenu
from presentation_layer.new_student_menu import NewStudentMenu
from service_layer.student_service import StudentService


class Terminal(BaseTerminal):
    menu_map: dict

    def __init__(self, student_service: StudentService):
        self.menu_map = {
            "main_menu": MainMenu(self),
            "new_student_menu": NewStudentMenu(self)
        }
        self.navigate("main_menu")
        self.running = True
        self.student_service = student_service

    def navigate(self, menu_name: str):
        self.current_menu = self.menu_map.get(menu_name)

    def quit(self):
        self.running = False
        print("Quitting...")

