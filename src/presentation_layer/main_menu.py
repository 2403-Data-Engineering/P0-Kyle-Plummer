from presentation_layer.base_menu import BaseMenu



class MainMenu(BaseMenu):
    def render(self) -> None:
        print("""
===========================
Welcome to uRevature Admin
1) Create new student
2) Create new professor
3) GET STUDENT 1
4) Enroll student in class
5) Run report
Q) Quit
        """)

        user_input: str = input().lower()
        match user_input:
            case "1":
                print("DEBUG: navigating...", self, self.terminal)
                self.terminal.navigate("new_student_menu")
            case "2":
                print("TODO: IMPLEMENT ME")
            case "3":
                self.terminal.student_service.get_by_id()
            case "4":
                print("TODO: IMPLEMENT ME")
            case "5":
                print("TODO: IMPLEMENT ME")
            case "q":
                self.terminal.quit()
                  