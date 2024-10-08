# Generated by Django 5.1.1 on 2024-09-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JIRAField',
            fields=[
                ('name', models.CharField()),
                ('field_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('schema_json', models.CharField()),
                ('description', models.CharField()),
                ('key', models.CharField()),
                ('stable_id', models.CharField()),
                ('is_locked', models.BooleanField()),
                ('searcherKey', models.CharField()),
            ],
        ),
    ]
