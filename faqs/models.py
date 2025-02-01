from django.db import models
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator
from django.core.cache import cache

class FAQ(models.Model):
    question_en = models.TextField()
    answer_en = RichTextField()

    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Override the save method to handle translations."""
        if not self.question_hi:
            self.question_hi = GoogleTranslator(source='en', target='hi').translate(self.question_en)
        if not self.question_bn:
            self.question_bn = GoogleTranslator(source='en', target='bn').translate(self.question_en)
        
        if not self.answer_hi:
            self.answer_hi = GoogleTranslator(source='en', target='hi').translate(self.answer_en)
        if not self.answer_bn:
            self.answer_bn = GoogleTranslator(source='en', target='bn').translate(self.answer_en)
        
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """Return the translated question based on language."""
        cache_key = f"faq_{self.id}_question_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        if lang == 'hi':
            translation = self.question_hi or self.question_en
        elif lang == 'bn':
            translation = self.question_bn or self.question_en
        else:
            translation = self.question_en

        cache.set(cache_key, translation, timeout=3600)
        return translation

    def get_translated_answer(self, lang='en'):
        """Return the translated answer based on language."""
        cache_key = f"faq_{self.id}_answer_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        if lang == 'hi':
            translation = self.answer_hi or self.answer_en
        elif lang == 'bn':
            translation = self.answer_bn or self.answer_en
        else:
            translation = self.answer_en

        cache.set(cache_key, translation, timeout=3600)
        return translation

    def __str__(self):
        return self.question_en