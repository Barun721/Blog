# Generated by Django 4.2.3 on 2023-07-27 03:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(related_name='group_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
