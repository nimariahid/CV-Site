# Generated by Django 3.0.7 on 2020-06-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_framework'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillcategory',
            name='collapse',
            field=models.BooleanField(default=False),
        ),
    ]
