# Generated by Django 2.1.1 on 2018-11-01 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fest',
            name='logo',
            field=models.ImageField(upload_to='static/imagess'),
        ),
    ]
