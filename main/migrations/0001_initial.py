# Generated by Django 3.1.6 on 2021-06-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('emailId', models.EmailField(max_length=150)),
                ('phoneNumber', models.IntegerField()),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
