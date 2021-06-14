# Generated by Django 3.2.4 on 2021-06-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew_shareapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brewmethod',
            options={},
        ),
        migrations.AlterModelOptions(
            name='entryflag',
            options={},
        ),
        migrations.AlterModelOptions(
            name='recipereview',
            options={},
        ),
        migrations.AlterModelOptions(
            name='recommendrecipe',
            options={},
        ),
        migrations.AddField(
            model_name='entry',
            name='coffee_amount',
            field=models.IntegerField(default=35),
            preserve_default=False,
        ),
    ]