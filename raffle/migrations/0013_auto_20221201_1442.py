# Generated by Django 3.2 on 2022-12-01 14:42

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('raffle', '0012_auto_20221201_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_content',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(blank=True),
        ),
    ]
