# Generated by Django 3.0.10 on 2020-10-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_like',
            new_name='users_like',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
    ]
