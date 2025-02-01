from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer_en': CKEditorWidget(),
            'answer_hi': CKEditorWidget(),
            'answer_bn': CKEditorWidget(),
        }

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question_en', 'question_hi', 'question_bn', 'answer_en', 'answer_hi', 'answer_bn')
    search_fields = ('question_en', 'question_hi', 'question_bn')  # Allows search
    list_filter = ('question_en', 'question_hi', 'question_bn')  # Filtering in admin

    fieldsets = (
        ('🔹 English (Default)', {'fields': ('question_en', 'answer_en')}),
        ('🔹 Hindi (Translated)', {'fields': ('question_hi', 'answer_hi')}),
        ('🔹 Bengali (Translated)', {'fields': ('question_bn', 'answer_bn')}),
    )