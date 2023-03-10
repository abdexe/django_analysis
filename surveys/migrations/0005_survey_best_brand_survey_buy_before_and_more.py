# Generated by Django 4.1.4 on 2022-12-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_survey_user_age_survey_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='best_brand',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='survey',
            name='buy_before',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='survey',
            name='hear_brand',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='survey',
            name='other_brand',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='survey',
            name='rating_experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='rating_feedback',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='see_brand',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='survey',
            name='sharing_probabilite',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='speaking_brand',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='survey',
            name='use_before',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='survey',
            name='comment',
            field=models.TextField(default='null'),
        ),
    ]
