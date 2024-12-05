from app import SchoolSystem

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("خطأ: الرجاء إدخال رقم صحيح.")

def main():
    system = SchoolSystem()
    while True:
        print("\nالرجاء اختيار العملية التي تريد إجرائها:")
        print("* لإضافة طالب اضغط على a")
        print("* لحذف طالب اضغط على d")
        print("* لتعديل بيانات طالب اضغط على u")
        print("* لعرض بيانات طالب اضغط على s")
        print("* لإضافة درس اضغط على al")
        print("* لحذف درس اضغط على dl")
        print("* لعرض جميع الدروس اضغط على ll")
        print("* لإنهاء البرنامج اضغط على q")

        choice = input("أدخل الخيار: ").strip().lower()

        if choice == 'a':
            student_id = get_valid_int("أدخل رقم الطالب: ")
            first_name = input("أدخل الاسم الأول: ")
            last_name = input("أدخل الكنية: ")
            age = get_valid_int("أدخل العمر: ")
            grade = input("أدخل الصف: ")
            registration_date = input("أدخل تاريخ التسجيل (YYYY-MM-DD): ")
            system.list_lessons()
            lesson_ids = list(map(int, input("أدخل معرفات الدروس مفصولة بفواصل: ").split(",")))
            system.add_student(student_id, first_name, last_name, age, grade, registration_date, lesson_ids)

        elif choice == 'd':
            student_id = get_valid_int("أدخل رقم الطالب لحذفه: ")
            system.delete_student(student_id)

        elif choice == 'u':
            student_id = get_valid_int("أدخل رقم الطالب لتعديل بياناته: ")
            first_name = input("أدخل الاسم الأول الجديد (أو اتركه فارغًا): ") or None
            last_name = input("أدخل الكنية الجديدة (أو اتركه فارغًا): ") or None
            age = input("أدخل العمر الجديد (أو اتركه فارغًا): ")
            grade = input("أدخل الصف الجديد (أو اتركه فارغًا): ") or None
            registration_date = input("أدخل تاريخ التسجيل الجديد (أو اتركه فارغًا): ") or None

            system.update_student(
                student_id,
                first_name,
                last_name,
                int(age) if age.isdigit() else None,
                grade,
                registration_date
            )

        elif choice == 's':
            student_id = get_valid_int("أدخل رقم الطالب لعرض معلوماته: ")
            system.show_student(student_id)

        elif choice == 'al':
            lesson_name = input("أدخل اسم الدرس الجديد: ")
            system.add_lesson(lesson_name)

        elif choice == 'dl':
            lesson_id = get_valid_int("أدخل معرف الدرس لحذفه: ")
            system.delete_lesson(lesson_id)

        elif choice == 'll':
            system.list_lessons()

        elif choice == 'q':
            print("إنهاء البرنامج...")
            break

        else:
            print("خيار غير صالح، حاول مرة أخرى.")

if __name__ == "__main__":
    main()
