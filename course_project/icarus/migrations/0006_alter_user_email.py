# Generated by Django 4.1.7 on 2023-05-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("icarus", "0005_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Email Address"),
        ),
    ]