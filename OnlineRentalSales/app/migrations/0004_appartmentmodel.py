# Generated by Django 2.1.4 on 2019-01-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190129_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppartmentModel',
            fields=[
                ('appartmentno', models.IntegerField(primary_key=True, serialize=False)),
                ('flatno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('noofflats', models.IntegerField()),
            ],
        ),
    ]
