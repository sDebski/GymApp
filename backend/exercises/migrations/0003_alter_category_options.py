# Generated by Django 4.2.3 on 2023-08-04 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_rename_post_comment_exercise'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name']},
        ),
    ]