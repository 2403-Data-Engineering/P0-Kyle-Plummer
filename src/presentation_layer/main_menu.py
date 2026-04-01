from presentation_layer.menu import Menu
from presentation_layer.new_student_menu import NewStudentMenu
from presentation_layer.terminal import MenuEnum


class MainMenu(Menu):
    def render(self) -> None:
        print("""
===========================
Welcome to uRevature Admin
1) Create new student
2) Create new professor
3) Create new class
4) Enroll student in class
5) Run report
Q) Quit
        """)

        user_input: str = input().lower()
        match user_input:
            case "1":
                self.terminal.navigate(MenuEnum.NEW_STUDENT_MENU)
            case "2":
                print("TODO: IMPLEMENT ME")
            case "3":
                print("TODO: IMPLEMENT ME")
            case "4":
                print("TODO: IMPLEMENT ME")
            case "5":
                print("TODO: IMPLEMENT ME")
            case "q":
                self.terminal.quit()
                  