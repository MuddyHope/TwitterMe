# Generated by Django 4.1.3 on 2022-11-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=250, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]