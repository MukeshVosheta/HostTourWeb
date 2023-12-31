# Generated by Django 4.2.6 on 2023-11-04 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_reviewpack_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewpack',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('w_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.packages')),
            ],
        ),
    ]
