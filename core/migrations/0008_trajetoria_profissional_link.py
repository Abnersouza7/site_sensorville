# Generated by Django 5.0.1 on 2024-01-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_certificate_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='trajetoria_profissional',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
    ]
