# Generated by Django 3.2 on 2022-11-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffle', '0004_post_hook_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sc_image',
            field=models.ImageField(blank=True, upload_to='raffle/images/%Y/%m/%d/'),
        ),
    ]
