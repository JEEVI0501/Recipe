# Generated by Django 4.1.6 on 2023-03-31 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0004_user_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='username',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
