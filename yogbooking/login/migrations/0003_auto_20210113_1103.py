# Generated by Django 3.0.7 on 2021-01-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210109_1220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userregister',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='resume',
            field=models.FileField(default='', upload_to='yogbookingapp/pdf'),
        ),
    ]