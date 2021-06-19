# Generated by Django 3.2.4 on 2021-06-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew_shareapi', '0009_alter_brewmethod_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewer',
            name='current_brew_method',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='brewer',
            name='current_coffee',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='brewer',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='review',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tasting_notes',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='entryreport',
            name='resolution',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='entrystep',
            name='step_image',
            field=models.ImageField(blank=True, null=True, upload_to='coffee_pics/%Y/%m/%d'),
        ),
    ]