# Generated by Django 4.2 on 2023-12-12 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        ("homework", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="enrollment",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="course",
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="student",
        ),
        migrations.AlterField(
            model_name="homework",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.course"
            ),
        ),
        migrations.DeleteModel(
            name="Course",
        ),
        migrations.DeleteModel(
            name="Enrollment",
        ),
    ]
