# Generated by Django 3.1.1 on 2020-09-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default=0, max_length=500),
        ),
    ]