# Generated by Django 4.0.4 on 2022-07-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0007_alter_studentprofile_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='student_profile', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='nationality',
            field=models.CharField(default='Nigerian', max_length=10, null=True),
        ),
    ]