# Generated by Django 5.0 on 2024-02-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_category_alter_recipe_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(default='minutos', max_length=65),
        ),
    ]