# Generated by Django 2.0.7 on 2018-07-30 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
                ('contents', models.TextField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
