# Generated by Django 4.1.3 on 2022-11-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='viajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Viajesfamiliares',
        ),
    ]