# Generated by Django 2.0.3 on 2018-10-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20181030_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye fotoğraf ekleyin'),
        ),
    ]
