# Generated by Django 4.2.2 on 2023-08-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование компании'),
        ),
    ]