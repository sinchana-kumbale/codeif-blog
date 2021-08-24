# Generated by Django 3.2.6 on 2021-08-24 19:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0006_alter_post_users_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Users_views',
            field=models.ManyToManyField(default=3, related_name='Users_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
