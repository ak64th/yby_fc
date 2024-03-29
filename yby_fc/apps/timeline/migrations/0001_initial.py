# Generated by Django 2.2.4 on 2019-08-22 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
            ],
            options={
                'verbose_name': 'post',
            },
        ),
    ]
