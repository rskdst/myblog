# Generated by Django 2.1.7 on 2019-07-22 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leaveword', '0002_auto_20190719_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='level',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_to', to='Leaveword.UserMessage'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_id', to='Leaveword.UserMessage'),
        ),
    ]
