# Generated by Django 3.2.6 on 2021-08-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_rename_name_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]