#test of for loops

students = {}

students[001] = "Arild Heyyland";
students[002] = "Turid Hoeyland";
students[003] = "Oddrun H. Heyyland";
students[004] = "Harald Heyyland";
students[005] = "Signe Heyyland";
students[006] = "Arne Heyyland";
students[007] = "Ivar Heyyland";

def search_students(student_no):
    for key in students:
        if key == student_no:
            return students[key]
    return "No student with that number found"

def find_student(student_no):
    print search_students(student_no)


find_student(0037)
