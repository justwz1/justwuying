# Generated by Django 2.2.5 on 2023-11-24 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20231124_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peopleinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo'),
        ),
    ]
