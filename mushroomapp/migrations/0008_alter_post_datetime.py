# Generated by Django 3.2.23 on 2023-12-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroomapp', '0007_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
