# Generated by Django 4.2 on 2023-04-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('about', models.TextField()),
                ('student_image', models.ImageField(upload_to='student_image')),
            ],
        ),
    ]
