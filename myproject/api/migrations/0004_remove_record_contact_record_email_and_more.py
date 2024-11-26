# Generated by Django 4.2.11 on 2024-11-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_record_contact_users_email_alter_users_mobilenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='contact',
        ),
        migrations.AddField(
            model_name='record',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
