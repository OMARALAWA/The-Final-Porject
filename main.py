from app import SchoolSystem


def main():
    system = SchoolSystem()
    while True:
        print("الرجاء اختيار العملية التي تريد إجرائها:")
        print("* لإضافة طالب إضغط على حرف a")
        print("* لحذف طالب إضغط على حرف d")
        print("* لتعديل معلومات طالب إضغط على حرف u")
        print("* لعرض معلومات طالب إضغط على حرف s")
        choice = input("أدخل الخيار: ").strip().lower()

        if choice == 'a':
            student_id = int(input("أدخل رقم الطالب: "))
            first_name = input("أدخل الاسم الأول: ")
            last_name = input("أدخل الكنية: ")
            age = int(input("أدخل العمر: "))
            grade = input("أدخل الصف: ")
            registration_date = input("أدخل تاريخ التسجيل (YYYY-MM-DD): ")
            lessons = input("أدخل أسماء الدروس، مفصولة بفواصل: ").split(",")
            system.add_student(student_id, first_name, last_name, age, grade, registration_date, lessons)

        elif choice == 'd':
            student_id = int(input("أدخل رقم الطالب لحذفه: "))
            system.delete_student(student_id)

        elif choice == 'u':
            student_id = int(input("أدخل رقم الطالب لتعديل معلوماته: "))
            first_name = input("أدخل الاسم الأول الجديد (أو اتركه فارغًا): ") or None
            last_name = input("أدخل الكنية الجديدة (أو اتركه فارغًا): ") or None
            age = input("أدخل العمر الجديد (أو اتركه فارغًا): ") or None
            grade = input("أدخل الصف الجديد (أو اتركه فارغًا): ") or None
            system.update_student(student_id, first_name, last_name, int(age) if age else None, grade)

        elif choice == 's':
            student_id = int(input("أدخل رقم الطالب لعرض معلوماته: "))
            system.show_student(student_id)

        else:
            print("الرجاء اختيار خيار صالح")


if __name__ == "__main__":
    main()
