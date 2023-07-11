# Generated by Django 4.2.3 on 2023-07-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setcollect', '0004_alter_conversation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='title_tag',
            field=models.ManyToManyField(to='setcollect.tag'),
        ),
        migrations.AlterField(
            model_name='lmodel',
            name='lmodel',
            field=models.SmallIntegerField(choices=[(1, 'ChatGPT'), (2, 'ChatGLM'), (3, 'Bard'), (4, 'Human')], verbose_name='choice of model'),
        ),
    ]
