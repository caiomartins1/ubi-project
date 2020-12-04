# Generated by Django 3.1.3 on 2020-12-03 17:00

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='contract',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('is_parent', models.BooleanField(default=False)),
                ('is_institutional', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
            ],
            options={
                'verbose_name': 'content',
            },
        ),
    ]
