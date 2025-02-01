from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation_creation(self):
        faq = FAQ.objects.create(
            question_en="What is Python?",
            answer_en="<p>Python is a programming language.</p>"
        )
        self.assertNotEqual(faq.question_hi, "")
        self.assertNotEqual(faq.answer_hi, "")

class FAQAPITest(TestCase):
    def setUp(self):
        FAQ.objects.create(
            question_en="Test Question",
            answer_en="<p>Test Answer</p>"
        )

    def test_api_response(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Question", response.data[0]['question'])
