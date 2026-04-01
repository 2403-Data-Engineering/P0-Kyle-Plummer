from models.student import Student

class StudentService:

    def save(self, student: Student) -> Student:
        print("TODO: Implement the student service save method....")
        print("...for now pretend that worked.")
        print("STUDENT SAVED!")

    def get_by_id(id: int) -> Student:
        # Dummy Data:
        return Student(id, first_name="Test", last_name="User", email="test.email@email.com", major="Something", year="Something")
