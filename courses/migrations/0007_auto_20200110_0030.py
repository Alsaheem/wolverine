# Generated by Django 3.0 on 2020-01-09 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_currentsemester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CurrentSemester',
        ),
    ]