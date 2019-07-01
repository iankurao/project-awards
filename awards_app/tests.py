from django.test import TestCase
from .models import Projects,Profile,Comments
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


class TestProfile(TestCase):
    def setUp(self):
        self.new_profile=Profile(profile='iano',bio='I love code',phone="0723475550")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_initialization(self):
        self.assertEqual(self.new_profile.profile,'iano')
        self.assertEqual(self.new_profile.bio,'I love code')
        self.assertEqual(self.new_profile.phone,"0723475550")  

class TestComments(TestCase):
    def setUp(self):
        self.new_comment=Comments(comment="Amazing",pro_id=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comments))

    def test_initialization(self):
        self.assertEqual(self.new_comment.comment,"Amazing")
        self.assertEqual(self.new_comment.pro_id,0)

