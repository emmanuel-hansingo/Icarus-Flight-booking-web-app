# Generated by Django 4.1.7 on 2023-05-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("icarus", "0004_rename_username_user_password_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]