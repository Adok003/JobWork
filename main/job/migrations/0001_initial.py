# Generated by Django 4.0.5 on 2022-06-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(null=True)),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('director', 'director'), ('senior', 'senior'), ('middle', 'middle'), ('junior', 'junior'), ('ordinary', 'ordinary')], max_length=50)),
                ('hire_date', models.DateField()),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'Employees',
            },
        ),
    ]
