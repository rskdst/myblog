# Generated by Django 2.1.7 on 2019-07-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userinfo', '0002_auto_20190719_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]