# Generated by Django 2.2 on 2019-05-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrawingsTrackerApp', '0007_auto_20190520_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawings',
            name='code_Id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='date_submitted',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='drawings',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
