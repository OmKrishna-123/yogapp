# Generated by Django 3.0.7 on 2021-01-15 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210115_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='email',
            new_name='user',
        ),
    ]
