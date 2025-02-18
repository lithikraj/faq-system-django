# Generated by Django 4.2.4 on 2025-01-31 17:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer_bn',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_hi',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
