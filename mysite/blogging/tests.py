from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post

class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json']
    
    def setUp(self):
        self.user = User.objects.get(pk=1)
        
    def test_strung_representation(self):
        excepted = "This is a title"
        p1 = Post(title=excepted)
        actual = str(p1)
        self.assertEqual(excepted, actual)
        
