from dataclasses import dataclass
from typing import List, Optional
from datetime import date

@dataclass
class Student:
    student_id: str
    name: str
    date_of_birth: date
    enrolled_courses: List['Course'] = None

    def __post_init__(self):
        if self.enrolled_courses is None:
            self.enrolled_courses = []

    def enroll(self, course: 'Course') -> None:
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def __str__(self) -> str:
        return f"Student: {self.name} (ID: {self.student_id})"

@dataclass
class Course:
    course_id: str
    title: str
    credits: int
    department: Optional['Department'] = None
    students: List[Student] = None

    def __post_init__(self):
        if self.students is None:
            self.students = []

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def __str__(self) -> str:
        return f"Course: {self.title} (ID: {self.course_id}, Credits: {self.credits})"

@dataclass
class Department:
    dept_id: str
    name: str
    courses: List[Course] = None

    def __post_init__(self):
        if self.courses is None:
            self.courses = []

    def add_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
            course.department = self

    def __str__(self) -> str:
        return f"Department: {self.name} (ID: {self.dept_id})"