# Generated by Django 4.2.6 on 2023-10-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_tourmoreplaces_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourmoreplaces',
            name='link',
            field=models.TextField(max_length=1000),
        ),
    ]