import sqlite3


class Database:
    def __init__(self):
        # إنشاء اتصال بقاعدة البيانات
        self.connection = sqlite3.connect("school.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        # إنشاء جدول الطلاب
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

        # إنشاء جدول الدروس
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                lesson_id INTEGER PRIMARY KEY,
                lesson_name TEXT
            )
        """)

        # إنشاء جدول العلاقة بين الطلاب والدروس
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_lessons (
                student_id INTEGER,
                lesson_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id),
                FOREIGN KEY(lesson_id) REFERENCES lessons(lesson_id),
                PRIMARY KEY (student_id, lesson_id)
            )
        """)

        self.connection.commit()
        print("تم إنشاء الجداول بنجاح.")

    # دالة لإضافة طالب جديد مع شرط العمر بين 6 و 30
    def add_student(self, student_id, first_name, last_name, age, grade, registration_date, lesson_ids):
        if age < 6 or age > 30:
            print("خطأ: العمر يجب أن يكون بين 6 و 30 سنة.")
            return

        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO students (student_id, first_name, last_name, age, grade, registration_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id, first_name, last_name, age, grade, registration_date))

        for lesson_id in lesson_ids:
            cursor.execute("INSERT INTO student_lessons (student_id, lesson_id) VALUES (?, ?)", (student_id, lesson_id))

        self.connection.commit()
        print("تمت إضافة الطالب بنجاح.")

    # دالة لتحديث بيانات الطالب مع شرط العمر بين 6 و 30
    def update_student(self, student_id, first_name=None, last_name=None, age=None, grade=None):
        if age is not None:
            if age < 6 or age > 30:
                print("خطأ: العمر يجب أن يكون بين 6 و 30 سنة.")
                return

        cursor = self.connection.cursor()
        if first_name:
            cursor.execute("UPDATE students SET first_name = ? WHERE student_id = ?", (first_name, student_id))
        if last_name:
            cursor.execute("UPDATE students SET last_name = ? WHERE student_id = ?", (last_name, student_id))
        if age:
            cursor.execute("UPDATE students SET age = ? WHERE student_id = ?", (age, student_id))
        if grade:
            cursor.execute("UPDATE students SET grade = ? WHERE student_id = ?", (grade, student_id))

        self.connection.commit()
        print("تم تعديل بيانات الطالب بنجاح.")

    def close_connection(self):
        self.connection.close()


# اختبار الوظائف
if __name__ == "__main__":
    db = Database()


