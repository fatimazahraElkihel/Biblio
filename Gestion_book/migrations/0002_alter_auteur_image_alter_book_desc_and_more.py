# Generated by Django 4.2.1 on 2023-06-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auteur',
            name='image',
            field=models.ImageField(upload_to='client/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Desc',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='book',
            name='Edition',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='Titre',
            field=models.CharField(max_length=100),
        ),
    ]