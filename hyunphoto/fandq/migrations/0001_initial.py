# Generated by Django 4.2.15 on 2024-08-22 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'db_table': 'fandq_category',
            },
        ),
        migrations.CreateModel(
            name='Fandq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=200)),
                ('answer', models.TextField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fandq.category')),
            ],
            options={
                'verbose_name': 'fandq',
                'verbose_name_plural': 'fandqs',
                'db_table': 'fandq',
            },
        ),
    ]
