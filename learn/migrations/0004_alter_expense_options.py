# Generated by Django 4.0.6 on 2022-07-28 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_rename_catagory_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]
