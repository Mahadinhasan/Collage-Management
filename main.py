from entities import Student, Course, Department
from reports import ReportGenerator, ConsoleReport, CSVReport
from utils import get_valid_string, get_valid_date, get_valid_int
from typing import List
from datetime import date

class CollegeManager:
    def __init__(self):
        self.students: List[Student] = []
        self.courses: List[Course] = []
        self.departments: List[Department] = []
        self.report_generators: List[ReportGenerator] = [ConsoleReport(), CSVReport()]

    def add_student(self, student_id: str, name: str, dob: date) -> None:
        student = Student(student_id, name, dob)
        self.students.append(student)

    def add_course(self, course_id: str, title: str, credits: int) -> None:
        course = Course(course_id, title, credits)
        self.courses.append(course)

    def add_department(self, dept_id: str, name: str) -> None:
        dept = Department(dept_id, name)
        self.departments.append(dept)

    def enroll_student(self, student_idx: int, course_idx: int) -> None:
        if 0 <= student_idx < len(self.students) and 0 <= course_idx < len(self.courses):
            self.students[student_idx].enroll(self.courses[course_idx])
            print("Enrollment successful.")
        else:
            print("Invalid student or course index.")

    def assign_course_to_dept(self, course_idx: int, dept_idx: int) -> None:
        if 0 <= course_idx < len(self.courses) and 0 <= dept_idx < len(self.departments):
            self.departments[dept_idx].add_course(self.courses[course_idx])
            print("Course assigned to department.")
        else:
            print("Invalid course or department index.")

    def generate_report(self, data_type: str) -> None:
        data_map = {
            "students": (self.students, "Student Report"),
            "courses": (self.courses, "Course Report"),
            "departments": (self.departments, "Department Report")
        }
        if data_type in data_map:
            data, title = data_map[data_type]
            for generator in self.report_generators:
                generator.generate(data, title)
        else:
            print("Invalid report type.")

def main():
    manager = CollegeManager()
    while True:
        print("\nCollege Management System:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Department")
        print("4. Enroll Student in Course")
        print("5. Assign Course to Department")
        print("6. Generate Report")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            student_id = get_valid_string("Student ID: ")
            name = get_valid_string("Student Name: ")
            dob = get_valid_date("Date of Birth")
            manager.add_student(student_id, name, dob)
            print("Student added.")
        elif choice == "2":
            course_id = get_valid_string("Course ID: ")
            title = get_valid_string("Course Title: ")
            credits = get_valid_int("Credits (1-6): ", 1, 6)
            manager.add_course(course_id, title, credits)
            print("Course added.")
        elif choice == "3":
            dept_id = get_valid_string("Department ID: ")
            name = get_valid_string("Department Name: ")
            manager.add_department(dept_id, name)
            print("Department added.")
        elif choice == "4":
            print("\nStudents:")
            for i, student in enumerate(manager.students, 1):
                print(f"{i}. {student}")
            print("\nCourses:")
            for i, course in enumerate(manager.courses, 1):
                print(f"{i}. {course}")
            try:
                student_idx = get_valid_int("Student number: ", 1, len(manager.students)) - 1
                course_idx = get_valid_int("Course number: ", 1, len(manager.courses)) - 1
                manager.enroll_student(student_idx, course_idx)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            print("\nCourses:")
            for i, course in enumerate(manager.courses, 1):
                print(f"{i}. {course}")
            print("\nDepartments:")
            for i, dept in enumerate(manager.departments, 1):
                print(f"{i}. {dept}")
            try:
                course_idx = get_valid_int("Course number: ", 1, len(manager.courses)) - 1
                dept_idx = get_valid_int("Department number: ", 1, len(manager.departments)) - 1
                manager.assign_course_to_dept(course_idx, dept_idx)
            except ValueError:
                print("Invalid input.")
        elif choice == "6":
            print("Report types: students, courses, departments")
            report_type = get_valid_string("Enter report type: ").lower()
            manager.generate_report(report_type)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()