import pytest
from faqs.models import FAQ

@pytest.mark.django_db  # Allow database access for the test functions
def test_faqs_in_english(client):  # Use 'client' instead of 'api_client'
    faq_data = [
        FAQ.objects.create(
            question_en="What is Django?",       
            answer_en="Django is a high-level Python web framework.",
            question_hi="क्या है Django?",       
            answer_hi="Django एक उच्च-स्तरीय पायथ थन वेब ढांचा है।",
            question_bn="Django কী?", 
            answer_bn="Django একটি উচ্চ-স্তরের পা াইথন ওয়েব ফ্রেমওয়ার্ক।"
        )
    ]
    
    response = client.get('/api/faqs/')  # Replace with the actual URL of your API
    assert response.status_code == 200
    # Add other assertions based on the expected behavior

@pytest.mark.django_db  # Allow database access for the test functions
def test_faqs_in_hindi(client):  # Use 'client' instead of 'api_client'
    faq_data = [
        FAQ.objects.create(
            question_en="What is Django?",       
            answer_en="Django is a high-level Python web framework.",
            question_hi="क्या है Django?",       
            answer_hi="Django एक उच्च-स्तरीय पायथ थन वेब ढांचा है।",
            question_bn="Django কী?", 
            answer_bn="Django একটি উচ্চ-স্তরের পা াইথন ওয়েব ফ্রেমওয়ার্ক।"
        )
    ]
    
    response = client.get('/api/faqs/')  # Replace with the actual URL of your API
    assert response.status_code == 200
    # Add other assertions based on the expected behavior

@pytest.mark.django_db  # Allow database access for the test functions
def test_faqs_in_bengali(client):  # Use 'client' instead of 'api_client'
    faq_data = [
        FAQ.objects.create(
            question_en="What is Django?",       
            answer_en="Django is a high-level Python web framework.",
            question_hi="क्या है Django?",       
            answer_hi="Django एक उच्च-स्तरीय पायथ थन वेब ढांचा है।",
            question_bn="Django কী?", 
            answer_bn="Django একটি উচ্চ-স্তরের পা াইথন ওয়েব ফ্রেমওয়ার্ক।"
        )
    ]
    
    response = client.get('/api/faqs/')  # Replace with the actual URL of your API
    assert response.status_code == 200
    # Add other assertions based on the expected behavior