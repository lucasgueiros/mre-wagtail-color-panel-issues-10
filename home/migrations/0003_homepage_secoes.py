# Generated by Django 4.1.5 on 2023-01-24 15:19

from django.db import migrations
import wagtail.fields
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='secoes',
            field=wagtail.fields.StreamField([('cor', wagtail_color_panel.blocks.NativeColorBlock())], null=True, use_json_field=None),
        ),
    ]
