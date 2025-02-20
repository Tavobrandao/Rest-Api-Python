# Generated by Django 5.1.6 on 2025-02-20 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AulasConcluidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('faixa_atual', models.CharField(choices=[('B', 'Branca'), ('A', 'Azul'), ('R', 'Roxa'), ('M', 'Marrom'), ('P', 'Preta')], default='B', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treino.alunos')),
            ],
        ),
    ]
