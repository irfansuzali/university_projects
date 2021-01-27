# Generated by Django 3.1.5 on 2021-01-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210126_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'schools',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='school',
            field=models.CharField(default='University of Illinois Urbana Champaign', max_length=255),
            preserve_default=False,
        ),
    ]
