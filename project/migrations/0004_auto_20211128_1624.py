# Generated by Django 3.2.8 on 2021-11-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_reccomended_reps_exercise_recommended_reps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='total_time',
        ),
        migrations.AddField(
            model_name='schedule',
            name='end_time',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='start_time',
            field=models.TextField(blank=True),
        ),
    ]
