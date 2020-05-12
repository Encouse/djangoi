# Generated by Django 2.2.10 on 2020-05-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='id',
        ),
        migrations.AlterField(
            model_name='interview',
            name='name',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
