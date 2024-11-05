import sqlite3


class Database:
    def __init__(self):
        # انشاء اتصال بـ قاعدة البيانات
        self.connection = sqlite3.connect("school.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        # انشاء جدول students في قاعدة البيانات
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                grade TEXT,
                registration_date TEXT
            )
        """)

        # انشاء جدول lessons في قاعدة البيانات
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                lesson_id INTEGER PRIMARY KEY,
                lesson_name TEXT 
            )
        """)


        # انشاء جدول المشترك بين students and lessons لتخزين البيانات
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_lessons (
                student_id INTEGER,
                lesson_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id),
                FOREIGN KEY(lesson_id) REFERENCES lessons(lesson_id),
                PRIMARY KEY (student_id, lesson_id)  -- To prevent duplicates
            )
        """)

        # الدالة المسؤولة عن اتنفيذ التغييريات
        self.connection.commit()
        print("Tables created successfully.")


    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    db = Database()
    db.close_connection()
