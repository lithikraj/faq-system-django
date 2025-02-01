# faqs/urls.py
from django.urls import path
from .views import FAQList

urlpatterns = [
    path('', FAQList.as_view(), name='faq-list'),
]