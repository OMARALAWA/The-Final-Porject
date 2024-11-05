from database import Database

class SchoolSystem(Database):
    def __init__(self):
        super().__init__()
        # تم استخدام دالة الوراثة التابعة لـ Database

    def add_student(self, student_id, first_name, last_name, age, grade, registration_date, lessons):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO students (student_id, first_name, last_name, age, grade, registration_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (student_id, first_name, last_name, age, grade, registration_date))
        # هنا تم استخدام الطريقة المتعارف عليها و هي التي تشبه المستخدمة في برنامج SQLite

        for lesson in lessons:
            cursor.execute("INSERT INTO lessons (lesson_name) VALUES (?)", (lesson,))
            lesson_id = cursor.lastrowid
            # الحصول على المعرف
            cursor.execute("INSERT INTO student_lessons (student_id, lesson_id) VALUES (?, ?)", (student_id, lesson_id))
            # تم استخدام List comprehension

        self.connection.commit()
        # عند استخدام commit اذا هنا نريد ان نحفظ التغيرات
        print("تمت إضافة الطالب بنجاح")


    def delete_student(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        cursor.execute("DELETE FROM student_lessons WHERE student_id = ?", (student_id,))
        self.connection.commit()
        print("تم حذف الطالب بنجاح")

    def update_student(self, student_id, first_name=None, last_name=None, age=None, grade=None):
        # المعني بكلمة None هنا اي ان تركه فارغ حتى يتم ادخال القيمة من طرف المستخدم
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
        print("تم تحديث معلومات الطالب بنجاح")

    def show_student(self, student_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        # في بايثون، دالة cursor.fetchone() تُستخدم لاسترداد الصف التالي من نتائج استعلام قاعدة البيانات
        if student:
            cursor.execute("""
                SELECT lessons.lesson_name FROM lessons
                INNER JOIN student_lessons ON lessons.lesson_id = student_lessons.lesson_id
                WHERE student_lessons.student_id = ?
            """, (student_id,))
            # في بايثون، تستخدم ثلاث علامات تنصيص (""" أو ''') لتعريف نصوص متعددة الأسطر (multiline strings) دون الحاجة لاستخدام \n لإدخال فواصل الأسطر.
            lessons = cursor.fetchall()
            print("معلومات الطالب:")
            print(f"الاسم: {student[1]} {student[2]}, العمر: {student[3]}, الصف: {student[4]}, الدروس:", lessons)
        else:
            print("الطالب غير موجود")




#cursor.execute(f"""
    #INSERT INTO students (student_id, first_name, last_name, age, grade, registration_date)
    #VALUES ({student_id}, '{first_name}', '{last_name}', {age}, '{grade}', '{registration_date}')
#""")
# يمكن استخدام هذه الطريقة في ادخال بيانات الطلاب لاكن قد لا تكون آمنه