# Generated by Django 5.1.2 on 2024-10-09 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tarefa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicio', models.DateTimeField()),
                ('dt_fim', models.DateTimeField()),
                ('ds_descricao', models.TextField()),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('dt_alteracao', models.DateTimeField(auto_now=True, null=True)),
                ('fk_tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.tarefamodel')),
            ],
            options={
                'db_table': 'atividades',
            },
        ),
    ]
