# Generated by Django 4.1.4 on 2022-12-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companiees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companie',
            name='logo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
