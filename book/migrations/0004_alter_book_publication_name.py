# Generated by Django 4.0 on 2023-11-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_publication_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_name',
            field=models.CharField(choices=[('PB1', 'publication 1'), ('PB2', 'publication 2'), ('PB3', 'publication 3'), ('PB4', 'PUBLICATION 4')], max_length=3, null=True),
        ),
    ]
