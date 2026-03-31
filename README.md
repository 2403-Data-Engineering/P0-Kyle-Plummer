
def navigate(menu: Menu):
    current_menu = menu

running = True
current_menu = main_menu
while(running):
    current_menu.render()


def render():
    print("Enter a first name: ")
    first_name = input()
    print("Enter a last name: ")
    last_name = input()
    new_student = Student(first_name, last_name)
    navigate(New_)
