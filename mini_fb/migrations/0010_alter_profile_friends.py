# Generated by Django 3.2.8 on 2021-11-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0009_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_mini_fb_profile_friends_+', to='mini_fb.Profile'),
        ),
    ]