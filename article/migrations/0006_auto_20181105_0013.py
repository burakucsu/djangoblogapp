# Generated by Django 2.0.3 on 2018-11-04 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
    ]
