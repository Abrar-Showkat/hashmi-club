# Generated by Django 3.2.5 on 2021-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20210917_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='doj',
            field=models.DateField(blank=True, null=True),
        ),
    ]