from django.test import TestCase
from .models import Course
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the course model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.course_code = "test code"
        self.course = Course(code=self.course_code)
        self.course_section = "test section"
        self.course = Course(section=self.course_section)
        self.course_name = "test name"
        self.course = Course(name=self.course_name)
        self.course_semester = "test semester"
        self.course = Course(semester=self.course_semester)
        self.course_seats = "test seats"
        self.course = Course(seats=self.course_seats)
        self.course_instructor = "test instructor"
        self.course = Course(instructor=self.course_instructor)

    def test_model_can_create_a_course(self):
        """Test the course model can create a course."""
        old_count = Course.objects.count()
        self.course.save()
        new_count = Course.objects.count()
        self.assertNotEqual(old_count, new_count)