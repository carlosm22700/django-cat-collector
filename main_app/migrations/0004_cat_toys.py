# Generated by Django 4.2.1 on 2023-06-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_feeding_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]