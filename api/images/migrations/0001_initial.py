# Generated by Django 4.1.4 on 2022-12-17 04:04

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resizing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.ImageField(blank=True, null=True, upload_to=images.models.input_upload_key)),
                ('output', models.ImageField(blank=True, null=True, upload_to=images.models.output_upload_key)),
            ],
        ),
    ]
