# Generated by Django 3.2.12 on 2023-03-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20230313_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-created_on']},
        ),
    ]
