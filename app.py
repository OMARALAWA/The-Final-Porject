from Database import Database

class SchoolSystem(Database):
    def __init__(self):
        super().__init__()

    # إضافة درس جديد
    def add_lesson(self, lesson_name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO lessons (lesson_name) VALUES (?)", (lesson_name,))
        self.connection.commit()
        print(f"تمت إضافة الدرس '{lesson_name}' بنجاح.")

    # حذف درس
    def delete_lesson(self, lesson_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM lessons WHERE lesson_id = ?", (lesson_id,))
        cursor.execute("DELETE FROM student_lessons WHERE lesson_id = ?", (lesson_id,))
        self.connection.commit()
        print(f"تم حذف الدرس ذو المعرف {lesson_id} بنجاح.")

    # عرض جميع الدروس
    def list_lessons(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM lessons")
        lessons = cursor.fetchall()
        print("قائمة الدروس:")
        for lesson in lessons:
            print(f"ID: {lesson[0]}, Lesson Name: {lesson[1]}")

    # إضافة طالب جديد
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

    # حذف طالب
    def delete_student(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        cursor.execute("DELETE FROM student_lessons WHERE student_id = ?", (student_id,))
        self.connection.commit()
        print("تم حذف الطالب بنجاح.")

    # تعديل بيانات طالب
    def update_student(self, student_id, first_name=None, last_name=None, age=None, grade=None, registration_date=None):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        if not student:
            print("خطأ: لا يوجد طالب بالمعرف المحدد.")
            return

        if age is not None:
            if age < 6 or age > 30:
                print("خطأ: العمر يجب أن يكون بين 6 و 30 سنة.")
                return

        if first_name:
            cursor.execute("UPDATE students SET first_name = ? WHERE student_id = ?", (first_name, student_id))
        if last_name:
            cursor.execute("UPDATE students SET last_name = ? WHERE student_id = ?", (last_name, student_id))
        if age is not None:
            cursor.execute("UPDATE students SET age = ? WHERE student_id = ?", (age, student_id))
        if grade:
            cursor.execute("UPDATE students SET grade = ? WHERE student_id = ?", (grade, student_id))
        if registration_date:
            cursor.execute("UPDATE students SET registration_date = ? WHERE student_id = ?", (registration_date, student_id))

        self.connection.commit()
        print("تم تعديل بيانات الطالب بنجاح.")

    # عرض بيانات طالب
    def show_student(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        if student:
            cursor.execute("""
                SELECT lessons.lesson_name FROM lessons
                INNER JOIN student_lessons ON lessons.lesson_id = student_lessons.lesson_id
                WHERE student_lessons.student_id = ?
            """, (student_id,))
            lessons = cursor.fetchall()
            print("معلومات الطالب:")
            print(
                f"الاسم: {student[1]} {student[2]}, العمر: {student[3]}, الصف: {student[4]}, تاريخ التسجيل: {student[5]}")
            print("الدروس:", [lesson[0] for lesson in lessons])
        else:
            print("الطالب غير موجود.")
