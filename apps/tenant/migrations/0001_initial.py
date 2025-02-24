# Generated by Django 4.2.6 on 2023-10-18 15:21

from django.db import migrations, models
import tenant.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cnpj', models.CharField(max_length=100, validators=[tenant.validators.validate_cnpj])),
                ('company_name', models.CharField(max_length=100)),
                ('domain', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('sub_domain', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
