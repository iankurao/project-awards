from django.test import TestCase
from .models import Projects
# Create your tests here.

class TestProjects(TestCase):
    def setUp(self):

        self.new_project=Projects(name='git',image='project.jpg',description='amazing',link='https:project',screen1='phoebe',screen2='kin')

    def test_instace(self):
        self.assertTrue(isinstance(self.new_project,Projects))

    def test_initialization(self):
        self.assertEqual(self.new_project.name,"git")
        self.assertEqual(self.new_project.image,"project.jpg")
        self.assertEqual(self.new_project.description,"amazing")
        self.assertEqual(self.new_project.link,"https:project")
        self.assertEqual(self.new_project.screen1,"phoebe")
        self.assertEqual(self.new_project.screen2,"kin")
