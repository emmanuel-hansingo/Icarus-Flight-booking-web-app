# Generated by Django 4.1.7 on 2023-05-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("icarus", "0006_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
