# Generated by Django 4.2 on 2023-04-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stp_resources', '0002_webresource_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='resources',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Problem',
        ),
        migrations.AlterField(
            model_name='webresource',
            name='Summary',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='question',
            name='problem',
            field=models.TextField(default='Null', max_length=100),
            preserve_default=False,
        ),
    ]
