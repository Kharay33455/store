# Generated by Django 4.2.10 on 2025-03-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_companyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyname',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
