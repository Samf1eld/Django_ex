# Generated by Django 4.1.7 on 2023-05-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openai_15', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_response',
            field=models.TextField(null=True, verbose_name='question response(answer) text'),
        ),
    ]