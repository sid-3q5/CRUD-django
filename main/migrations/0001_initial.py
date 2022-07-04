# Generated by Django 4.0.5 on 2022-07-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=100)),
                ('status2', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=9, null=True)),
                ('country', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]