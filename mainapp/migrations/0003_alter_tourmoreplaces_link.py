# Generated by Django 4.2.6 on 2023-10-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_tpack_name_packages_tourplace_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourmoreplaces',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]
