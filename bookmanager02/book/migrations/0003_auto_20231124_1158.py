# Generated by Django 2.2.5 on 2023-11-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_peopleinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
