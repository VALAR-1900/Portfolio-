# Generated by Django 3.0.5 on 2020-05-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200529_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contactdetails',
            new_name='email',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.TextField(blank=True),
        ),
    ]
