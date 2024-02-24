# Generated by Django 4.2.10 on 2024-02-24 12:42

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_color_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=[('#ff0000', 'qizil'), ('#ffa500', 'jigar rang'), ('#ffff00', 'sariq'), ('#008000', 'yashil'), ('#0000ff', "ko'k"), ('#4b0082', 'binafsha'), ('#ee82ee', 'pushti'), ('#000000', 'qora')]),
        ),
    ]
