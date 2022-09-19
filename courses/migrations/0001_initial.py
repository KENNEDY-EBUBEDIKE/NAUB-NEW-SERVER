# Generated by Django 4.0.4 on 2022-07-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=255, null=True, unique=True)),
                ('course_title', models.CharField(max_length=255, null=True, unique=True)),
                ('course_faculty', models.CharField(max_length=255, null=True)),
                ('course_department', models.CharField(max_length=255, null=True)),
                ('credit_unit', models.IntegerField(null=True)),
                ('course_type', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('course_code',),
            },
        ),
    ]