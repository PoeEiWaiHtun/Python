# Generated by Django 3.0.8 on 2020-07-07 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syskey', models.IntegerField(default=0, max_length=255)),
                ('createdDate', models.CharField(default='', max_length=255)),
                ('t1', models.CharField(default='', max_length=255)),
                ('t2', models.CharField(default='', max_length=255)),
                ('t5', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
