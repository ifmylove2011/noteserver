# Generated by Django 2.0.1 on 2018-01-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attach',
            name='_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
