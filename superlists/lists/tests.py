from django.test import TestCase

# Create your tests here.


class randTest(TestCase):

    def test_failiure(self):
        self.assertEqual(1+1, 3)
