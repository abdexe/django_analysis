# Generated by Django 4.1.4 on 2022-12-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, default='cairo', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, default='Male', max_length=150, null=True),
        ),
    ]
