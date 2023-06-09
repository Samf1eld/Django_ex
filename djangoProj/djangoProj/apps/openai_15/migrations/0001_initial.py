# Generated by Django 4.1.7 on 2023-05-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_name', models.CharField(max_length=200, verbose_name='name of the question')),
                ('q_request', models.TextField(verbose_name='question request text')),
                ('q_response', models.TextField(verbose_name='question response(answer) text')),
                ('q_date_req', models.DateTimeField(verbose_name='request date')),
                ('q_date_res', models.DateTimeField(verbose_name='response date')),
            ],
            options={
                'verbose_name': 'Question to AI',
                'verbose_name_plural': 'Questions to AI',
            },
        ),
    ]
