# Generated by Django 2.1 on 2018-10-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_auto_20181008_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_page',
            name='branch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course_page',
            name='degree',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course_page',
            name='exam',
            field=models.CharField(max_length=50),
        ),
    ]
