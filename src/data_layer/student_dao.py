from data_layer.db_connection_manager import get_connection


def get_student_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", [id])
        return cursor.fetchone()
    

