# Generated by Django 4.2.3 on 2023-07-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setcollect', '0002_question_userinfo_role_lmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lmodel',
            old_name='question_from',
            new_name='question',
        ),
    ]