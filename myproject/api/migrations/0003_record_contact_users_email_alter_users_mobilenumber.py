# Generated by Django 4.2.11 on 2024-11-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_record_users_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='contact',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='Mobilenumber',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]
