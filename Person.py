from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email  # Triggers the setter for validation

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        # Basic validation rule for email
        if "@" not in value or "." not in value:
            raise ValueError(f"Invalid email address: '{value}'")
        self._email = value

    @abstractmethod
    def role_info(self) -> str:
        """Abstract method to be implemented by subclasses."""
        pass

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Student(Person):
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id

    def role_info(self) -> str:
        return f"Role: Student | ID: {self.student_id}"

    def __str__(self):
        return f"[Student] {super().__str__()} - ID: {self.student_id}"


class Lecturer(Person):
    def __init__(self, name: str, email: str, staff_id: str):
        super().__init__(name, email)
        self.staff_id = staff_id

    def role_info(self) -> str:
        return f"Role: Lecturer | Staff ID: {self.staff_id}"

    def __str__(self):
        return f"[Lecturer] {super().__str__()} - Staff ID: {self.staff_id}"
    class Course:
    def __init__(self, course_name: str, lecturer: Lecturer):
        self.course_name = course_name
        self.lecturer = lecturer  # Composition: Course HAS A Lecturer
        self.students = []        # Composition: Course HAS Student objects

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Only Student objects can be added to this course.")

    def __str__(self):
        student_names = ", ".join([s.name for s in self.students]) or "None"
        return (f"Course: {self.course_name}\n"
                f"Instructor: {self.lecturer.name}\n"
                f"Enrolled Students: [{student_names}]")


