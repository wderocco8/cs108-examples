# Generated by Django 3.2.8 on 2021-11-02 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20211102_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.person'),
            preserve_default=False,
        ),
    ]
