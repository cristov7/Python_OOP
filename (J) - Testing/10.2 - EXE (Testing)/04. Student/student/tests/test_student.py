import unittest
from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student_1 = Student("Alex")
        self.student_2 = Student("Bob", {"OOP with Python": ["6"]})

    def test___init___successfully(self):
        student_1_name = self.student_1.name
        expected_student_1_name = "Alex"
        self.assertEqual(student_1_name, expected_student_1_name)
        student_1_courses = self.student_1.courses
        expected_student_1_courses = {}
        self.assertEqual(student_1_courses, expected_student_1_courses)
        # student_2_name = self.student_2.name
        # expected_student_2_name = "Bob"
        # self.assertEqual(student_2_name, expected_student_2_name)
        student_2_courses = self.student_2.courses
        expected_student_2_courses = {"OOP with Python": ["6"]}
        self.assertEqual(student_2_courses, expected_student_2_courses)

    def test_enroll_and_notes_have_been_updated_successfully(self):
        result = self.student_2.enroll("OOP with Python", ["5", "6"])
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(result, expected_result)
        student_2_courses = self.student_2.courses
        expected_student_2_courses = {"OOP with Python": ["6", "5", "6"]}
        self.assertEqual(student_2_courses, expected_student_2_courses)

    def test_enroll_without_add_course_notes_and_add_course_with_notes_successfully(self):
        result = self.student_1.enroll("Programming Advanced with Python", ["5", "6"])
        expected_result = "Course and course notes have been added."
        self.assertEqual(result, expected_result)
        student_1_courses = self.student_1.courses
        expected_student_1_courses = {"Programming Advanced with Python": ["5", "6"]}
        self.assertEqual(student_1_courses, expected_student_1_courses)

    def test_enroll_with_add_course_notes_and_add_course_with_notes_successfully(self):
        result = self.student_1.enroll("Programming Advanced with Python", ["5", "6"], "Y")
        expected_result = "Course and course notes have been added."
        self.assertEqual(result, expected_result)
        student_1_courses = self.student_1.courses
        expected_student_1_courses = {"Programming Advanced with Python": ["5", "6"]}
        self.assertEqual(student_1_courses, expected_student_1_courses)

    def test_enroll_and_course_has_been_added_successfully(self):
        result = self.student_2.enroll("Programming Fundamentals with Python", ["2"], "N")
        expected_result = "Course has been added."
        self.assertEqual(result, expected_result)
        student_2_courses = self.student_2.courses
        expected_student_2_courses = {"OOP with Python": ["6"], "Programming Fundamentals with Python": []}
        self.assertEqual(student_2_courses, expected_student_2_courses)

    def test_add_notes_successfully(self):
        result = self.student_2.add_notes("OOP with Python", "6")
        expected_result = "Notes have been updated"
        self.assertEqual(result, expected_result)
        student_2_courses = self.student_2.courses
        expected_student_2_courses = {"OOP with Python": ["6", "6"]}
        self.assertEqual(student_2_courses, expected_student_2_courses)

    def test_add_notes_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.student_1.add_notes("OOP with Python", "6")
        result = str(content.exception)
        expected_result = "Cannot add notes. Course not found."
        self.assertEqual(result, expected_result)
        student_1_courses = self.student_1.courses
        expected_student_1_courses = {}
        self.assertEqual(student_1_courses, expected_student_1_courses)

    def test_leave_course_and_course_has_been_removed_successfully(self):
        result = self.student_2.leave_course("OOP with Python")
        expected_result = "Course has been removed"
        self.assertEqual(result, expected_result)
        student_2_courses = self.student_2.courses
        expected_student_2_courses = {}
        self.assertEqual(student_2_courses, expected_student_2_courses)

    def test_leave_course_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.student_1.leave_course("OOP with Python")
        result = str(content.exception)
        expected_result = "Cannot remove course. Course not found."
        self.assertEqual(result, expected_result)
        student_1_courses = self.student_1.courses
        expected_student_1_courses = {}
        self.assertEqual(student_1_courses, expected_student_1_courses)


if __name__ == '__main__':
    unittest.main()
