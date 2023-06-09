# Generated by Django 4.2 on 2023-04-21 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stp_resources', '0007_question_tag_webresource_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.CharField(choices=[('Student', 'I am a Student'), ('Teacher', 'I am a Teacher'), ('Parent', 'I am a Parent')], default='Student', max_length=20),
        ),
        migrations.AlterField(
            model_name='webresource',
            name='tag',
            field=models.CharField(choices=[('Student', 'I am a Student'), ('Teacher', 'I am a Teacher'), ('Parent', 'I am a Parent')], default='Parent', max_length=20),
        ),
        migrations.CreateModel(
            name='AnswerSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stp_resources.post')),
            ],
        ),
    ]
