# Generated by Django 5.1 on 2024-09-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp3', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
